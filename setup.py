from setuptools import setup

setup(
    name='s3ctl',
    version='0.1.12',
    author='Jonathan Morais',
    author_email='jonathan.lucena@zoom.com.br',
    license='MIT',
    packages=['src'],
    description='s3ctl is using for get info about s3 buckets',
    install_requires=["boto3", "botocore", "click"]
)
