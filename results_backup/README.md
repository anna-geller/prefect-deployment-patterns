# Results Q&A

## What are Results broadly speaking?
Return values of a task or flow. 

## Is configuration of Results needed to pass data between tasks or flows? 

No. Prefect has a first-class support for passing data between tasks and even between subflows. This means that there is no need for extra Result backend to pass data within your dataflow. It _just_ works out of the box. 


## Why Prefect _usually_ doesn't store results? 

- they can be large and slow to send to and from the API
- they can contain private information or data
- they need to be stored somewhere (DB, S3, etc.) - thanks to the hybrid execution model respecting your privacy & security, Prefect doesn't store your code or data within the backend database; only metadata that references the Result object is persisted

## If Prefect doesn't store results, where are those persisted?

Within your infrastructure - Prefect only stores a _reference_ to the result including:
- the storage block used to persist results (e.g. `s3/prod`)
- location within that remote storage (e.g. S3 object path `s3://bucket/file.pickle`)

## When Does Prefect store results directly in the DB?

With booleans (True, False) and nulls (None). Why? Because it reduces the overhead required to persist such simple information. There is a special result type called `ResultLiteral` for such values. Similarly, there is a special result type called `ResultReference` used by Prefect to store result metadata in the Prefect backend database. More on those special result types in the final section.


### Can I disable this? 👆

Yes, by setting ``persist_result`` to False. 

## Which features require Results persistence?

- Task **cache keys** 
- Flow/task run **retries** if a given task or flow returns data and needs to pass it to other tasks or flows 

---
# Configuring results - `persist_result`

## What do you need to configure?

1. Storage block - `result_storage`
2. Serializer - `result_serializer`
3. Boolean flag - `persist_result`

> 💡 Note that all of these arguments are optional. Prefect sets sensible defaults inferred from the context of how you interact with Prefect (e.g. retries, or caching). 

## When do I need to configure results? 

You only need to customize the above-mentioned result components to configure a specific type of storage (S3, GCS, ...), or serializer, or to disable persistence for specific tasks or flows. 

## What can be configured on the `@task` and `@flow` decorators?

- `persist_result`: persist to storage or not 
- `result_storage`: where to store the result e.g. `s3/prod` storage block
- `result_serializer`: how to convert the result to a storable form 

## How to toggle results on or off?
By using `persist_result=True` on a `@task` or `@flow` decorators. 

```python
import pandas as pd 
from prefect import flow, task

@task(persist_result=False)
def my_task() -> pd.DataFrame:
    print("Big dataframe ⛔️ disabling results")

@flow(persist_result=True, retries=2)
def my_flow():
    my_task()
```

### What happens when you set `persist_result=True`?

Results (i.e. return values) of such task or flow will be persisted even if there is no feature (such as `retries` or `caching`) that would require those.

### What happens when you set `persist_result=False`?
Results (i.e. return values) of such task or flow will NEVER be persisted even if there is a feature (such as `retries` or `caching`) that could potentially require those. In such scenario, an error will be raised.

> 📓 **TLDR:** Toggling persistence manually will always override any default or inferred behavior.

---
# Result storage - `result_storage`

## What is `result_storage` responsible for?
For reading and writing serialized data to an external location using one of the supported file system blocks.

## How to configure `result_storage`?

1. Using the `block_type/block_name` (i.e. the storage block slug)

```python
from prefect import flow, task

@task
def my_task():
    return "Hi! 👋"
    
@flow(persist_result=True, result_storage="s3/prod")
def my_flow():
    my_task()  # This task will use the flow's result storage
```

2. Using a specific (not saved to the API) storage block:

```python
from prefect import flow, task
from prefect.filesystems import LocalFileSystem, S3


@task(persist_result=True, result_storage=S3(bucket_path="bucket/path"))
def my_task():
    return "Hi! 👋"
    
@flow(persist_result=True, result_storage=LocalFileSystem(basepath="../results"))
def my_flow():
    my_task()  
```

---
# `result_storage` examples in form of a quiz 

Q1: Where will Prefect store results of `my_task` and when?

```python
from prefect import flow, task

@task
def my_task():
    return "Hi! 👋"
    
@flow(persist_result=True, result_storage="s3/prod")
def my_flow():
    my_task()  
```

<details>
  <summary>Answer</summary>

This task will infer result settings from the flow, because no explicit `persist_result` or `result_storage` have been configured on the task, i.e. it will always persist results to S3, even though this task doesn't use retries or caching. 

</details>

Q2: Where will Prefect store results of `my_task` and when?

```python
from prefect import flow, task

@task(persist_result=False, retries=3)
def my_task():
    return "Hi! 👋"
    
@flow(persist_result=True, result_storage="s3/prod")
def my_flow():
    my_task()  
```

<details>
  <summary>Answer</summary>

Even though `my_flow` will always persist results to S3, this task explicitly disables persistence. It's unlikely that `my_task` doing nothing but returning Hi would fail, retries won't work due to disabled persistence -- Prefect will raise an error during a retry attempt. 

</details>

Q3: Where will Prefect store results of `my_flow` and when? How about `my_task`?

```python
import pandas as pd
from prefect import flow, task

@task
def my_task() -> pd.DataFrame:
    print("Big dataframe ⛔️")

@flow(retries=2)
def my_flow():
    my_task()
```

<details>
  <summary>Answer</summary>

Given that `my_flow` has retries, Prefect will leverage default Result persistence mechanism for the flow, but the results of `my_task` will not be persisted since it doesn't need that (no retries, caching, etc.) and doesn't have any `persist_result` or `result_storage` overrides.

</details>



--- 
# Result serializers - `result_serializer`

## What is `result_serializer` responsible for?

For converting your Python object to and from bytes. This is necessary to store the object outside of the execution environment and retrieve it later.


## How to configure `result_serializer`?

To configure the result serializer, you may use:

- a string of a serializer type (such as `json` or `pickle`), e.g. `result_serializer="json"` or `result_serializer="pickle"` — this corresponds to an instance with default values
- an instance of a serializer with custom values set for that particular serializer class, e.g. `result_serializer=JSONSerializer(jsonlib="orjson")`

Example:

```python
from prefect import flow, task
from prefect.filesystems import LocalFileSystem, S3
from prefect.serializers import JSONSerializer

@task(persist_result=True, result_storage=S3(bucket_path="bucket/path"), result_serializer="pickle")
def my_task():
    return "Hi! 👋"
    
@flow(persist_result=True, result_storage=LocalFileSystem(basepath="../results"), result_serializer=JSONSerializer(jsonlib="orjson"))
def my_flow():
    my_task()  
```

## What are examples of supported `result_serializer` types?

1. Pickle serializer
2. JSON serializer

### What is Pickle serializer and what are its pros and cons?

Pickle is a standard Python protocol for encoding arbitrary Python objects. We provide a custom pickle serializer at `prefect.serializers.PickleSerializer`. Prefect's pickle serializer uses the [cloudpickle](https://github.com/cloudpipe/cloudpickle) project by default to support more object types. Alternative pickle libraries can be specified, as shown here:

```python
from prefect.serializers import PickleSerializer

PickleSerializer(picklelib="custompickle")
```

#### What are the benefits of the pickle serializer

- Many object types are supported.
- Objects can define custom pickle support.

#### What are the drawbacks of the pickle serializer

- When nested attributes of an object cannot be pickled, it is hard to determine the cause.
- When deserializing objects, your Python and pickle library versions must match the one used at serialization time.
- Serialized objects cannot be easily shared across different programming languages.
- Serialized objects are not human-readable.


### What is JSON serializer and what are its pros and cons?

We provide a custom JSON serializer at `prefect.serializers.JSONSerializer`. Prefect's JSON serializer uses custom hooks by default to support more object types. Specifically, we add support for all types supported by [Pydantic](https://pydantic-docs.helpmanual.io/).

By default, we use the standard Python `json` library. Alternative JSON libraries can be specified:

```python
from prefect.serializers import JSONSerializer

JSONSerializer(jsonlib="orjson")
```

#### What are the benefits of the JSON serializer

- Serialized objects are human readable.
- Serialized objects can often be shared across different programming languages.
- Deserialization of serialized objects is generally version agnostic.


#### What are the drawbacks of the JSON serializer

- Supported types are limited.
- Implementing support for additional types must be done at the serializer level.


--- 
## Default configuration

### What is the default `persist_result` and why?

`None`, because it automatically enables persistence when needed, e.g.:
- when a task has a `cache_key_fn` which requires that the value of a `cache_key` (which might contain sensitive information) must be stored
- when a task or flow has `retries` 

> 💡 TMYK: Technically, retries are possible without `Results` if the task doesn't return data that must be passed to downstream tasks or flows, but to make retries _fail-safe_, we require Results to be either configured explicitly or to be used implicitly by leveraging the default storage block and serializer.


### What is the default `result_storage` and why?

`None`, because Prefect automatically **infers** storage from the **context**. **Tasks** use the result storage configured on the **flow** (_unless otherwise specified_). 

If there is **no context** to load the storage from and results must be persisted (e.g. to enable retries or caching), results will be stored in the `.prefect-results` directory in the run's working directory.


### What is the default `result_serializer` and why?

By now, it won't be a surprise. The default value is `None`! Why?

Because, again, it's inferred from the **context**. **Tasks** will use the result serializer configured on the **flow** (_unless otherwise specified_). 

If there is **no context** to load the serializer from, the serializer defined by `PREFECT_RESULTS_DEFAULT_SERIALIZER` will be used. This setting defaults to Prefect's pickle serializer.

---
# Extra: how does Prefect store the reference to results under the hood?

Circling back to the question from the beginning regarding special result types that Prefect uses to hold a reference to each object, there are two such result types:

1. `ResultLiteral`
1. `ResultReference`


When the `result()` method is used on states or futures, Prefect internally calls a `get()` method to return the value of the result.


## What is `ResultLiteral`?

Stores booleans (True, False) and nulls (None) directly in the DB for performance reasons. The values contained by these results must always be JSON serializable.


Example:

```python
result = ResultLiteral(value=None)
result.json()
# {"type": "result", "value": "null"}
```


## What is `ResultReference`?
Contains information needed to retrieve the result from storage. This includes:

- `Key`: indicates where this specific result is in storage.
- `Storage`: a reference to the storage block used to write and read the result
- `Serializer`: serializer type and configuration used to (de)serialize the result.

The `get()` method on `ResultReference`: 
- retrieves the data from storage, 
- deserializes it, 
returns the original object. 

It will cache the resolved object to reduce the overhead of subsequent calls.

