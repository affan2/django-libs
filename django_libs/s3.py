"""Custom S3 storage backends to store files in subfolders."""
from django.core.files.storage import get_storage_class

from storages.backends.s3boto3 import S3Boto3Storage


class CachedS3BotoStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            'compressor.storage.CompressorFileStorage')()

    def save(self, name, content, max_length=None):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name


def CompressorS3BotoStorage():
    return CachedS3BotoStorage(location='compressor')


def MediaRootS3BotoStorage():
    return S3Boto3Storage(location='media')
