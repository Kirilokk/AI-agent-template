from typing import Any
import httpx

from src.constants import NWS_API_BASE, USER_AGENT


class WeatherService:
    """Service for interacting with the National Weather Service API."""

    def __init__(self, user_agent: str = USER_AGENT, base_url: str = NWS_API_BASE):
        self.base_url = base_url
        self.headers = {"User-Agent": user_agent, "Accept": "application/geo+json"}

    async def get_weather_data(self, url: str) -> dict[str, Any] | None:
        """Make a request to the NWS API with proper error handling."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=self.headers, timeout=30.0)
                response.raise_for_status()
                return response.json()
            except Exception:
                return None

    def format_alert(self, feature: dict) -> str:
        """Format an alert feature into a readable string."""
        props = feature["properties"]
        return (
            f"Event: {props.get('event', 'Unknown')}\n"
            f"Area: {props.get('areaDesc', 'Unknown')}\n"
            f"Severity: {props.get('severity', 'Unknown')}\n"
            f"Description: {props.get('description', 'No description available')}\n"
            f"Instructions: {props.get('instruction', 'No specific instructions provided')}"
        )
