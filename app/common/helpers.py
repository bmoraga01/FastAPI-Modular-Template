import base64
import uuid
from datetime import UTC, datetime
from pathlib import Path

from app.core.config import settings

# helpers for common tasks


def generate_uuid(length: int = 24):
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")[:length]


def get_utc_now() -> datetime:
    return datetime.now(UTC)


def generate_image_url(
    object_key: str, base_url: str = "http://localhost:8000"
) -> str:
    """
    Transforma una ruta absoluta de un objeto en la URL completa accesible públicamente.
    """

    absolute_path = Path(object_key)

    try:
        parts = absolute_path.parts
        upload_index = parts.index(settings.LOCAL_STORAGE_DIR)

        relative_path = Path(*parts[upload_index + 1 :])
    except ValueError:
        relative_path = absolute_path.name

    return f"{base_url}/images/{relative_path.as_posix()}"
