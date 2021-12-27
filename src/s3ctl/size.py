import boto3

client = boto3.client('s3')

def buckets_number_size(buckets):
    bckt_size = []

    for i in buckets:
        size = client.list_objects_v2(
            Bucket=i).get('Contents')[0]['Size']
        bckt_size.append(size)

    return bckt_size
