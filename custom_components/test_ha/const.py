"""Constants for test_ha."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "test_ha"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"

CONF_UPDATE_INTERVAL_HOURS = "update_interval_hours"

DEFAULT_UPDATE_INTERVAL_HOURS = 1.0
