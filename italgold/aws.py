from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = 'italgoldstaticassets'
    signature_version = 's3v4'
    querystring_auth = True
    gzip = True
    default_acl = 'public_read'
