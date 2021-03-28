from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = 'italgold'
    location = 'static'
    querystring_auth = True
    gzip = True
    default_acl = 'public_read'
