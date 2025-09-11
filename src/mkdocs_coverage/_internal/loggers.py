from __future__ import annotations

try:
    from mkdocs.plugins import get_plugin_logger as _get_plugin_logger
except ImportError:
    # TODO: remove once support for MkDocs <1.5 is dropped
    import logging
    from typing import TYPE_CHECKING, Any

    if TYPE_CHECKING:
        from collections.abc import MutableMapping

    class _PrefixedLogger(logging.LoggerAdapter):
        def __init__(self, prefix: str, logger: logging.Logger) -> None:
            super().__init__(logger, {})
            self.prefix = prefix

        def process(self, msg: str, kwargs: MutableMapping[str, Any]) -> tuple[str, Any]:
            return f"{self.prefix}: {msg}", kwargs

    def _get_plugin_logger(name: str) -> _PrefixedLogger:  # type: ignore[misc]
        logger = logging.getLogger(f"mkdocs.plugins.{name}")
        return _PrefixedLogger(name.split(".", 1)[0], logger)
