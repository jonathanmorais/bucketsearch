import boto3

s3 = boto3.resource('s3')

try:
    def buckets_number_obj(self, buckets):

        self.bucket_obj = []

        for bucket in buckets:
            self.count_obj = sum(1 for i in s3.Bucket(bucket).objects.all())
            self.bucket_obj.append(self.count_obj)

        return self.bucket_obj
except:
    print("error")
