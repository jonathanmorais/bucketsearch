import logging
from jawas.cli import bucket_summarize

logging.info('jawas working')


try:
    bucket_summarize([])

except Exception as err:
    print(err)
