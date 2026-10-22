"""The table of providers, written out: adding a rental service is one entry here and one module like `runpod.py`."""

from __future__ import annotations

from collections.abc import Callable

from virtual_unstaging.provision.errors import ProvisionError
from virtual_unstaging.provision.provider import Provider
from virtual_unstaging.provision.runpod import RunpodProvider
from virtual_unstaging.provision.transport import Transport

# name -> constructor taking the service's API key and the transport.
PROVIDERS: dict[str, Callable[[str, Transport], Provider]] = {
    "runpod": lambda key, transport: RunpodProvider(key, transport),
}


def provider_names() -> list[str]:
    return sorted(PROVIDERS)


def make_provider(name: str, api_key: str, transport: Transport) -> Provider:
    factory = PROVIDERS.get(name)
    if factory is None:
        raise ProvisionError("provider_unknown", f"no provider named {name!r}", f"known: {', '.join(provider_names())}")
    return factory(api_key, transport)
