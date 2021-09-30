import logging
from jawas.cli import bucket_summarize

logging.info('jawas working')


try:
    bucket_summarize(['xerpa-connectors-staging', 'xerpay-fargate-cli',
                     'severino-staging-serverlessdeploymentbucket-rvpfeg3vef4n'])

except Exception as err:
    print(err)
