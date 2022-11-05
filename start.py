import boto3
import pathlib


AWS_REGION = "us-east-1"
S3_BUCKET_NAME = "maksimboto3test"
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
