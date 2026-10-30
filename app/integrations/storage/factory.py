from app.core.config import settings
from app.integrations.storage.services import (
    BaseStorageService,
    LocalStorageService,
)


class StorageServiceFactory:
    @staticmethod
    def get_storage_service() -> BaseStorageService:
        storage_type = settings.STORAGE_TYPE

        if storage_type == "local":
            base_dir = str(settings.BASE_DIR / settings.LOCAL_STORAGE_DIR)
            return LocalStorageService(base_dir=base_dir)
        # elif storage_type == "s3":
        #     # Implement S3 storage service initialization here
        #     pass
        # elif storage_type == "cloudflare_r2":
        #     # Implement Cloudflare R2 storage service initialization here
        #     pass
        # elif storage_type == "minio":
        #     # Implement MinIO storage service initialization here
        #     pass
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")
