# s3ctl
A simple tool for buckets analize.

for work, define some variables, example below:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

## example of usage
```
s3ctl --bucket <bucket_name>
```

## example of response

```json
{
"bucket-name": [
    "2019-04-29-20:36:54",
     "30",
    "4161"]
}
```