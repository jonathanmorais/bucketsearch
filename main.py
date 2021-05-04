import boto3
import json
import time

def bucket_name():

    s3 = boto3.resource('s3')
    bckt = []

    for bucket in s3.buckets.all():
        bckt.append(bucket.name)

    return bckt

def bucket_creation_date():

    s3 = boto3.client('s3')
    buckets = bucket_name()
    dates = []

    for bucket in range(len(buckets)):
        dates.append(s3.list_buckets()["Buckets"][bucket]["CreationDate"].strftime('%Y-%m-%d-%H:%M:%S'))

    # res = "\n".join("{} {}".format(x, y) for x, y in zip(buckets, dates))

    return print(dates)

def buckets_number_obj():

    s3 = boto3.resource('s3')
    buckets = bucket_name()
    count_obj = 0

    for bucket in buckets:
        for i in s3.Bucket(bucket).objects.all():
            count_obj = count_obj + 1

    print(bucket, count_obj)

buckets_number_obj()