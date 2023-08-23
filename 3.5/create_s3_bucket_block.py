from time import sleep
from prefect_aws import S3Bucket, AwsCredentials


def create_aws_creds_block():
    aws_acc_key = input('aws_access_key: ')
    aws_sec_key = input('aws_secret_key: ')
    # my_aws_creds_obj = AwsCredentials(
    #     aws_access_key_id="123abc", aws_secret_access_key="abc123"
    # )
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id=aws_acc_key, aws_secret_access_key=aws_sec_key
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)


def create_s3_bucket_block():
    s3_bucket_name = input("Enter S3 Bucket Name: ")
    aws_creds = AwsCredentials.load("my-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name=s3_bucket_name, credentials=aws_creds
    )
    my_s3_bucket_obj.save(name="awss3-bucket", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
