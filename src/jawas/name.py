import boto3


def bucket_name():

    s3 = boto3.resource('s3')
    bckt = []

    for bucket in s3.buckets.all():
        bckt.append(bucket.name)

    return bckt


if __name__ == "__main__":
    bucket_name()
