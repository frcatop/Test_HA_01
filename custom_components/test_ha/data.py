"""
Runtime data types for test_ha.

Access pattern: entry.runtime_data.client / entry.runtime_data.coordinator
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import TestHAApiClient
    from .coordinator import TestHADataUpdateCoordinator


type TestHAConfigEntry = ConfigEntry[TestHAData]


@dataclass
class TestHAData:
    """Runtime data stored on the config entry after a successful setup."""

    client: TestHAApiClient
    coordinator: TestHADataUpdateCoordinator
    integration: Integration
