import boto3
import botocore

from jawas.name import bucket_name

try:
    def bucket_creation_date(buckets):

        s3 = boto3.client('s3')
        dates = []

        for bucket in range(len(buckets)):
            dates.append(s3.list_buckets()[
                "Buckets"][bucket]["CreationDate"].strftime('%Y-%m-%d-%H:%M:%S'))

        return dates
except botocore.exceptions.ClientError as error:
    raise error
