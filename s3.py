
import boto3
import pathlib


AWS_REGION = "us-east-1"
S3_BUCKET_NAME = "maksimboto3test"
""""Show alll buckets"""
# resource = boto3.resource("s3", region_name=AWS_REGION)
# iterator = resource.buckets.all()
# print("Listing Amazon S3 Buckets:")
# for bucket in iterator:
#     print(f"-- {bucket.name}")

"""Create bucket """""
# resource = boto3.resource("s3", region_name=AWS_REGION)

# bucket_name = "radianttestmaximboto3bucket22"
# location = {'LocationConstraint': AWS_REGION}

# bucket = resource.create_bucket(
#     Bucket=bucket_name,
#     CreateBucketConfiguration=location)

# print("Amazon S3 bucket has been created")

""""Show alll buckets"""
# resource = boto3.resource("s3", region_name=AWS_REGION)
# iterator = resource.buckets.all()
# print("Listing Amazon S3 Buckets:")
# for bucket in iterator:
#     print(f"-- {bucket.name}")
""""Upload file on bucket """

BASE_DIR = pathlib.Path(__file__).parent.resolve()
x = r".\currency.txt"


from lib.currency import get_currency


URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
get_currency(URL)

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")

#upload_files(f"{BASE_DIR}\\demo.txt", S3_BUCKET_NAME)
#       
upload_files(x,S3_BUCKET_NAME ,'currency.txt')

"""""Dowload file from bucket"""

# s3_resource = boto3.resource("s3", region_name=AWS_REGION)
# s3_object = s3_resource.Object(S3_BUCKET_NAME, 'Test.py')
# s3_object.download_file(f'C:\sql\Test.py')