import awswrangler as wr
from prefect_aws.s3 import AwsCredentials

creds = AwsCredentials.load("prod")
session = creds.get_boto3_session()

wr.s3.to_parquet(boto3_session=session, ...)
