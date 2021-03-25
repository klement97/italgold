from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = 'italgoldstaticassets'
    querystring_auth = False
    gzip = True
    default_acl = 'public_read'
