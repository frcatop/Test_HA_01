"""Sensor entity for test_ha."""

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from custom_components.test_ha.entity import TestHAEntity
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.helpers.typing import StateType


@dataclass(frozen=True, kw_only=True)
class TestHASensorEntityDescription(SensorEntityDescription):
    """Describes a sensor and how to read it from coordinator data."""

    value_fn: Callable[[dict[str, Any]], StateType]


class TestHASensor(SensorEntity, TestHAEntity):
    """Sensor backed by one value in the coordinator payload."""

    entity_description: TestHASensorEntityDescription

    @property
    def native_value(self) -> StateType:
        """Return the value read from coordinator data."""
        return self.entity_description.value_fn(self.coordinator.data)
