from prefect.filesystems import RemoteFileSystem

fs = RemoteFileSystem(basepath="s3://prefect-orion/flows")
fs.write_path("foo", b"hello")
fs.save("s3")
