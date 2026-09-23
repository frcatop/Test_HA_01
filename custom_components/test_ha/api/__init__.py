"""
API package for test_ha.

Exception hierarchy:
    TestHAApiClientError (base)
    ├── TestHAApiClientCommunicationError (network/timeout)
    └── TestHAApiClientAuthenticationError (401/403)

The coordinator maps them onto ConfigEntryAuthFailed and UpdateFailed; nothing else
in the integration imports this package.
"""

from .client import (
    FAN_SPEEDS,
    TestHAApiClient,
    TestHAApiClientAuthenticationError,
    TestHAApiClientCommunicationError,
    TestHAApiClientError,
)

__all__ = [
    "FAN_SPEEDS",
    "TestHAApiClient",
    "TestHAApiClientAuthenticationError",
    "TestHAApiClientCommunicationError",
    "TestHAApiClientError",
]
