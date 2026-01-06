from src.iceberg_rest.settings import settings
from pyiceberg.catalog.sql import SqlCatalog


class Catalog:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = _create_catalog()
        return cls.instance


def _create_catalog():
    catalog = SqlCatalog(
        settings.CATALOG_NAME,
        **{
            "uri": settings.CATALOG_JDBC_URI,
            "warehouse": settings.CATALOG_WAREHOUSE,
            "s3.endpoint": settings.CATALOG_S3_ENDPOINT,
            "s3.access-key-id": settings.AWS_ACCESS_KEY_ID,
            "s3.secret-access-key": settings.AWS_SECRET_ACCESS_KEY,
            "s3.verify-ssl": "false",
            "py-io-impl": "pyiceberg.io.fsspec.FsspecFileIO",
            "s3fs.client_kwargs": '{"verify": false}',
        },
    )
    return catalog


def get_catalog() -> Catalog:
    return Catalog()
