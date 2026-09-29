# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2021, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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
        if html_file.suffix == ".html" and html_file.name != "index.html" and "test" not in html_file.name:
            text = html_file.read_text()
            assert not re.search("covcovindex", text)
            assert not re.search('href="index.html"', text)
