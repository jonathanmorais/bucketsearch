import logging
import click
from click.decorators import command
from sum import bucket_summarize
from sum import bucket_summarize

logging.info('s3ctl working')

try:
    @click.command()
    @click.option('--bucket', help='flag to recover bucket info.')
    def help(name):
        """Simple CLI that get buckets info."""
        click.echo('Hello %s!' % name)

    def print_help_msg(command):
        with click.Context(command) as ctx:
            click.echo(command.get_help(ctx))
    print_help_msg(help)        

    @click.command()
    @click.option('--bucket')
    def bucket(bucket):
        click.echo(bucket_summarize([bucket]))
        exit()
    bucket()    

except click.ClickException as err:
    print(err)
