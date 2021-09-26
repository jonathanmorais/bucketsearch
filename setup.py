from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='jawas',
    version='__version__',
    author='Jonathan Morais',
    author_email='jonathan.m.lucena@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jawas = jawas.src:main'
        ]
    },
    description='Jawas is using for get info about s3 buckets',
    install_requires=requirements

)
