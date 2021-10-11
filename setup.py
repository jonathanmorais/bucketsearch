from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='s3ctl',
    version='0.1.3',
    author='Jonathan Morais',
    author_email='jonathan.lucena@zoom.com.br',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            's3ctl = src.s3ctl:main'
        ]
    },
    description='s3ctl is using for get info about s3 buckets',
    install_requires=requirements

)
