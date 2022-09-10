from prefect.filesystems import RemoteFileSystem

fs = RemoteFileSystem(basepath="s3://prefect-orion/flows")
fs.save("s3")
# fs.write_path("foo", b"hello")
