import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_bucket_size(bucket_name, s3_client):
    """Calculate the size of an S3 bucket."""
    total_size = 0
    try:
        paginator = s3_client.get_paginator('list_objects_v2')
        operation_parameters = {'Bucket': bucket_name}

        for page in paginator.paginate(**operation_parameters):
            if 'Contents' in page:
                total_size += sum(obj['Size'] for obj in page['Contents'])

    except s3_client.exceptions.NoSuchBucket:
        print(f"Bucket {bucket_name} no longer exists.")
    except Exception as e:
        print(f"Error calculating size for bucket {bucket_name}: {e}")

    return total_size

def list_buckets_and_sizes():
    """List all S3 buckets and their sizes."""
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()

        if 'Buckets' in response:
            print(f"{'Bucket Name':<40} {'Size (Bytes)':>20}")
            print("-" * 60)

            for bucket in response['Buckets']:
                bucket_name = bucket['Name']
                size = get_bucket_size(bucket_name, s3)
                print(f"{bucket_name:<40} {size:>20}")

        else:
            print("No buckets found in your AWS account.")

    except NoCredentialsError:
        print("AWS credentials not found. Configure them and try again.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please check your configuration.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_buckets_and_sizes()
