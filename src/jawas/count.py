import boto3
from jawas.name import bucket_name


def buckets_number_obj():

    s3 = boto3.resource('s3')
    buckets = bucket_name()
    count_obj = 0

    for bucket in buckets:
        for i in s3.Bucket(bucket).objects.all():
            count_obj = count_obj + 1

    print(bucket, count_obj)
