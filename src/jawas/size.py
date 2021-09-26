import boto3
from name import bucket_name


def buckets_number_size():
    s3 = boto3.resource('s3')
    buckets = bucket_name()
    total_bytes = 0
    n = 0

    for bucket in buckets:
        for bkct in s3.Bucket(bucket).objects.all():

            total_bytes += bkct.size
            n += 1
            if n % 2000 == 0:
                print(n)
        total_gigs = total_bytes

    print("%s: %i bytes, %i objects" % (buckets, total_gigs, n))

    return total_gigs, n
