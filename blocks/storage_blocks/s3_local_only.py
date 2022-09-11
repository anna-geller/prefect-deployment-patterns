from prefect.filesystems import S3

s3_block = S3(bucket_path="prefect-orion/mydata")
s3_block.save("mydata", overwrite=True)
