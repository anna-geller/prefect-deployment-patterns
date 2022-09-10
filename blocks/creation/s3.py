from prefect.filesystems import S3

s3_block = S3(bucket_path="prefect-orion/qa")
s3_block.save("dev", overwrite=True)
