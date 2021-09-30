import logging
from jawas.count import buckets_number_obj
from jawas.name import bucket_name
from jawas.date import bucket_creation_date
from jawas.size import buckets_number_size


def bucket_summarize(buckets):
    for i in buckets:
        dt_criacao = bucket_creation_date(buckets)
    for k in buckets:
        size = buckets_number_size(buckets)

    res = "\n".join("{} {}".format(x, y)
                    for x, y in zip(dt_criacao, str(size)))

    print(res)
