import boto3
from jawas.name import bucket_name


def bucket_creation_date(buckets):

    s3 = boto3.client('s3')
    # buckets = bucket_name()
    dates = []

    for bucket in range(len(buckets)):
        dates.append(s3.list_buckets()[
                     "Buckets"][bucket]["CreationDate"].strftime('%Y-%m-%d-%H:%M:%S'))

    # res = "\n".join("{} {}".format(x, y) for x, y in zip(buckets, dates))

    # print(dates)

    return dates
