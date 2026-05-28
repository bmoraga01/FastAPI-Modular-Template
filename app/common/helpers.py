import uuid
import base64


def generate_uuid(length: int = 24):
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")[:length]
