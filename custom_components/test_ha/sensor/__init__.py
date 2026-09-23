"""Sensor platform for test_ha."""

from typing import TYPE_CHECKING

from .air_quality import ENTITY_DESCRIPTIONS as AIR_QUALITY_DESCRIPTIONS
from .diagnostic import ENTITY_DESCRIPTIONS as DIAGNOSTIC_DESCRIPTIONS
from .entity import TestHASensor

# Read-only platform: the coordinator already serializes the fetch.
PARALLEL_UPDATES = 0

if TYPE_CHECKING:
    from custom_components.test_ha.data import TestHAConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

ENTITY_DESCRIPTIONS = (*AIR_QUALITY_DESCRIPTIONS, *DIAGNOSTIC_DESCRIPTIONS)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: TestHAConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(TestHASensor(entry.runtime_data.coordinator, description) for description in ENTITY_DESCRIPTIONS)
