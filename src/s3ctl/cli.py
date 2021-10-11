import logging
from s3ctl.count import buckets_number_obj
from s3ctl.name import bucket_name
from s3ctl.date import bucket_creation_date
from s3ctl.size import buckets_number_size

try:
    def bucket_summarize(buckets):
        dt_criacao = bucket_creation_date(buckets)
        num_obj = buckets_number_obj(buckets)
        size_obj = buckets_number_size(buckets)
        res = dict()

        for key in buckets:
            for value in zip(dt_criacao, num_obj, size_obj):
                res[key] = [value]
                break
        print(res)

except TypeError:
    print('Error' + TypeError)
