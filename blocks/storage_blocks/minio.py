from prefect.filesystems import RemoteFileSystem

minio = RemoteFileSystem(
    basepath="s3://yourbucket/flows",
    settings={
        "key": "MINIO_ROOT_USER",
        "secret": "MINIO_ROOT_PASSWORD",
        "client_kwargs": {"endpoint_url": "http://localhost:9000"},
    },
)

minio.save("prod")
