import setuptools
from version import get_git_version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='s3ctl',
    version=get_git_version(),
    author='Jonathan Morais',
    author_email='jonathan.m.lucena@gmail.com.br',
    license='MIT',
    description='s3ctl is using for get info about s3 buckets',
    install_requires=["boto3", "click"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
