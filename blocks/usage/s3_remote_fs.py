from prefect.filesystems import RemoteFileSystem

fs = RemoteFileSystem.load("dev-s3")
fs.read_path("foo")  # b'hello'
