import boto3
import time

BUCKET_NAME = "NOME_DO_BUCKET"
FILE_TEST = "NOME_DO_ARQUIVO"
REGION = 'REGION'

def create_s3_client():
    try:
        return boto3.client(
            "s3"
        )
    except Exception as ex:
        print(ex)
        raise ex

def validate_bucket(s3_client):
    try:
        s3_client.head_bucket(Bucket=BUCKET_NAME)
        return True
    except Exception as ex:
        print(ex)
        return False

def create_bucket(s3_client):
    try:
        s3_client.create_bucket(
            ACL="private",
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={
                "LocationConstraint" : REGION
            }
        )
    except Exception as ex:
        print(ex)
        raise ex

def send_file(s3_client):
    file = open(FILE_TEST,'w')
    time_to_print = time.asctime(time.localtime(time.time()))
    print(f"Data available to print in a file: {time_to_print}")
    file.write(time_to_print)
    file.close()
    try:
        s3_client.upload_file(FILE_TEST, BUCKET_NAME, FILE_TEST)
    except Exception as ex:
        print(ex)
        raise ex

def read_file(s3_client):
    try:
        file = s3_client.get_object(Bucket=BUCKET_NAME, Key=FILE_TEST)
        content = file['Body'].read().decode("utf-8")
        print(f"Data from file: {content}")
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    client = create_s3_client()
    bucket_exists = (validate_bucket(client))
    if bucket_exists:
        print("Bucket exists!")
        send_file(client)
        read_file(client)
    else:
        print("Bucket NOK!")

