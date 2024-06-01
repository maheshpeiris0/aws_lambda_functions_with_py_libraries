import json
import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    # Replace 'your_bucket_name' and 'your_file_key' with your S3 bucket name and file key
    bucket_name = 'aa-glue-files-mp'
    file_key = 'employees_data.csv'  # Adjust the file extension if it's different

    try:
        # Get the file object
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)

        file_content = obj['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(file_content))

        df_json = df.to_json()

        return {
            'statusCode': 200,
            'body': json.dumps(df_json)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
