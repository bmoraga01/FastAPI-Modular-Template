import httpx

from app.common.exceptions import BadRequestException
from app.core.config import settings

SITEVERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"

TURNSTILE_SECRET = settings.TURNSTILE_SECRET


async def verify_turnstile_token(token: str, remote_ip: str) -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            SITEVERIFY_URL,
            data={
                "secret": TURNSTILE_SECRET,
                "response": token,
                "remoteip": remote_ip,
            },
        )

        result = response.json()

        if not result.get("success"):
            raise BadRequestException("Turnstile verification failed")

        if result.get("action") != "service-request":
            raise BadRequestException("Turnstile action mismatch")
