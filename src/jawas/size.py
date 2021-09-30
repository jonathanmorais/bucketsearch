import boto3
from jawas.name import bucket_name


def buckets_number_size(buckets):
    s3 = boto3.resource('s3')
    size = 0
    sizes = []

    for bucket in buckets:
        for o in s3.Bucket(bucket).objects.all():
            size += o.size
        size = "{:.2f} MB".format(size/1024/1024)

    return size
