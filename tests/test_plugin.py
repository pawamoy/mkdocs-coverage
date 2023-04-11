"""Tests for the plugin module."""

import re
from pathlib import Path

from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_plugin() -> None:
    """Build our own documentation."""
    config = load_config()
    config["plugins"].run_event("startup", command="build", dirty=False)
    try:
        build(config)
    finally:
        config["plugins"].run_event("shutdown")
    site_coverage_dir = Path(config["site_dir"]) / "coverage"
    for html_file in site_coverage_dir.iterdir():
        if html_file.suffix == ".html" and html_file.name != "index.html" and "tests" not in html_file.name:
            text = html_file.read_text()
            assert not re.search("covcovindex", text)
            assert not re.search('href="index.html"', text)
