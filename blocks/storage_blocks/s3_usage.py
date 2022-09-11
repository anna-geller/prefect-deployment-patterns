from prefect.filesystems import S3

s3_block = S3.load("mydata")
