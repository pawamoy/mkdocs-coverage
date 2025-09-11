"""Deprecated. Import from `mkdocs_coverage` directly."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from mkdocs_coverage._internal import loggers


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from `mkdocs_coverage.loggers` is deprecated. Import from `mkdocs_coverage` directly.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(loggers, name, getattr(loggers, f"_{name}"))
