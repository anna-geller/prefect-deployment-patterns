from prefect.filesystems import RemoteFileSystem

minio = RemoteFileSystem.load("prod")
