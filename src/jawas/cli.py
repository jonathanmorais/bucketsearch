import logging
from jawas.count import buckets_number_obj
from jawas.name import bucket_name
from jawas.date import bucket_creation_date
from jawas.size import buckets_number_size

try:
    def bucket_summarize(buckets):
        dt_criacao = bucket_creation_date(buckets)
        num_obj = buckets_number_obj(buckets)
        size_obj = buckets_number_size(buckets)
        res = dict()

        for key in buckets:
            for value in zip(dt_criacao, num_obj, size_obj):
                res[key] = [value]
                dt_criacao.remove(value[0])
                num_obj.remove(value[1])
                size_obj.remove(value[2])
                break
        print(res)

except TypeError:
    print('aqui1')
    print('Error' + TypeError)
