import shutil
from abc import ABC, abstractmethod
from pathlib import Path

from fastapi import UploadFile


class BaseStorageService(ABC):
    @abstractmethod
    async def upload_file(self, file: UploadFile, folder: str = "") -> str:
        """Saves files and return the route or URL public/identifier."""

    @abstractmethod
    async def delete_file(self, file_path: str) -> bool:
        """Deletes the file at the given path or key and returns True if successful."""


class LocalStorageService(BaseStorageService):
    def __init__(self, base_dir: str = "uploads"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    async def upload_file(self, file: UploadFile, folder: str = "") -> str:
        target_dir = self.base_dir / folder
        target_dir.mkdir(parents=True, exist_ok=True)

        file_path = target_dir / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return str(file_path)

    async def delete_file(self, file_path: str) -> bool:
        path = Path(file_path)

        if path.exists():
            path.unlink()
            return True
        return False
