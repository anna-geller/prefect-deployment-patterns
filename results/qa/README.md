# Flow-level results persistence

## ``persist_result=True``
- local, ``persist_result=True`` ✅
- local, ``persist_result=True``, json ✅
- local, ``persist_result=True``, pickle ✅
- local, ``persist_result=True``, orjson as example of a custom serializer class ✅
- s3, ``persist_result=True`` ✅
- s3, ``persist_result=True``, json ✅

## ``persist_result=False``
- local, ``persist_result=False``, no need to check serializers ✅
- s3, ``persist_result=False``, no need to check serializers ✅

## ``persist_result=None`` = inferred from the context

- local, ``persist_result=None`` ✅
- local, ``persist_result=None``, but using retries for a subflow ✅

# Task-level results persistence inferred from the flow

- local, ``persist_result=True`` -- task should also be persisted ✅
- local, ``persist_result=True`` on both task and flow -- both flow and task result should be persisted ✅
- local, ``persist_result=True`` on flow but `False` on task -- flow results is persisted, task is not ✅
- local, ``persist_result=False`` -- task should NOT be persisted, even if it needs it for retries ✅
- local, ``persist_result=None`` + task with retries -- task should be persisted ✅
- local, ``persist_result=None`` + task with caching -- task should be persisted ✅

# Task-level results persistence specified directly on the task

## ``persist_result=True``
- local, ``persist_result=True`` ✅
- local, ``persist_result=True``, json ✅
- local, ``persist_result=True``, pickle ✅
- local, ``persist_result=True``, orjson as example of a custom serializer class ✅
- s3, ``persist_result=True`` ✅

## ``persist_result=False``
- local, ``persist_result=False``, no need to check serializers ✅
- s3, ``persist_result=False``, no need to check serializers ✅

## ``persist_result=None`` = inferred from the context

- local, ``persist_result=None`` ✅
- local, ``persist_result=None``, but using retries ✅
- local, ``persist_result=None``, but using caching ✅

