import logging
import click
from s3ctl.cli import bucket_summarize
from s3ctl.cli import bucket_summarize

logging.info('s3ctl working')

try:
    @click.command()
    @click.option('--bucket')
    def output(bucket):
        click.echo(bucket_summarize([bucket]))

    output()
except click.ClickException as err:
    print(err)
