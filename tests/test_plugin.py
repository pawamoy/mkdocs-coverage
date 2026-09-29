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
from io import StringIO
from pathlib import Path

from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_plugin(tmp_path: Path) -> None:
    """Build a minimal site with an embedded coverage report."""
    # Create the documentation and coverage report without project build artifacts.
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "index.md").write_text("# Test", encoding="utf-8")

    html_report_dir = tmp_path / "htmlcov"
    html_report_dir.mkdir()
    (html_report_dir / "index.html").write_text('<a href="module.html">Module</a>', encoding="utf-8")
    (html_report_dir / "module.html").write_text('<a href="index.html">Index</a><a href="covindex.html">Index</a>', encoding="utf-8")

    # Load the configuration from memory instead of the project's documentation config.
    config = load_config(
        StringIO("site_name: Test"),
        docs_dir=str(docs_dir),
        site_dir=str(tmp_path / "site"),
        plugins=[{"coverage": {"html_report_dir": str(html_report_dir)}}],
    )

    config["plugins"].run_event("startup", command="build", dirty=False)
    try:
        build(config)
    finally:
        config["plugins"].run_event("shutdown")

    # Keep the coverage index separate from the page that embeds it, and rewrite report links.
    site_coverage_dir = Path(config["site_dir"]) / "coverage"
    assert (site_coverage_dir / "covindex.html").is_file()
    assert 'src="covindex.html"' in (site_coverage_dir / "index.html").read_text(encoding="utf-8")
    assert 'href="covindex.html"' in (site_coverage_dir / "module.html").read_text(encoding="utf-8")

    for html_file in site_coverage_dir.iterdir():
        if html_file.suffix == ".html" and html_file.name != "index.html" and "test" not in html_file.name:
            text = html_file.read_text(encoding="utf-8")
            assert not re.search("covcovindex", text)
            assert not re.search('href="index.html"', text)
