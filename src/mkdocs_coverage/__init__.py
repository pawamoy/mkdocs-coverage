"""MkDocs Coverage Plugin package.

MkDocs plugin to integrate your coverage HTML report into your site.
"""

from __future__ import annotations

from mkdocs_coverage._internal.plugin import MkDocsCoverageConfig, MkDocsCoveragePlugin

__all__: list[str] = ["MkDocsCoverageConfig", "MkDocsCoveragePlugin"]
