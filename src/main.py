import boto3
import json
import time
import subprocess
import os
import logging
from jawas.count import buckets_number_obj

logging.info('jawas working')


try:
    buckets_number_obj()
except Exception as err:
    print(err)
