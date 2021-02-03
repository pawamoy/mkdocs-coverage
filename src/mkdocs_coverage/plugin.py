"""This module contains the `mkdocs_coverage` plugin."""

import re
import shutil
import textwrap
from distutils.dir_util import copy_tree
from distutils.errors import DistutilsFileError
from pathlib import Path
from tempfile import mkdtemp
from typing import Sequence, Tuple

from mkdocs.config import Config
from mkdocs.config.config_options import Type as MkType
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files

from mkdocs_coverage.loggers import get_logger

log = get_logger(__name__)


class MkDocsCoveragePlugin(BasePlugin):
    """The MkDocs plugin to integrate the coverage HTML report in the site."""

    config_scheme: Sequence[Tuple[str, MkType]] = (
        ("page_name", MkType(str, default="coverage")),
        ("html_report_dir", MkType(str, default="htmlcov")),
    )

    def on_files(self, files: Files, config: Config, **kwargs) -> Files:
        """
        Add the coverage page to the navigation.

        Hook for the [`on_files` event](https://www.mkdocs.org/user-guide/plugins/#on_files).
        This hook is used to add the coverage page to the navigation, using a temporary file.

        Arguments:
            files: The files collection.
            config: The MkDocs config object.
            kwargs: Additional arguments passed by MkDocs.

        Returns:
            The modified files collection.
        """
        page_contents = textwrap.dedent(
            """
            <style>
            .md-content {
                max-width: none !important;
            }
            article h1, article > a {
                display: none;
            }
            </style>

            <script>
            function resizeIframe(obj) {
                obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 'px';
            }
            </script>

            <iframe src="covindex.html" frameborder="0" scrolling="no" onload="resizeIframe(this)" width="100%"></iframe>
            """,
        )
        tempdir = mkdtemp()
        page_name = self.config["page_name"] + ".md"
        tempfile = Path(tempdir) / page_name
        with tempfile.open("w") as fp:
            fp.write(page_contents)
        files.append(
            File(
                page_name,
                str(tempfile.parent),
                config["site_dir"],
                config["use_directory_urls"],
            ),
        )
        return files

    def on_post_build(self, config: Config, **kwargs) -> None:  # noqa: W0613,R0201 (unused arguments, cannot be static)
        """
        Copy the coverage HTML report into the site directory.

        Hook for the [`on_post_build` event](https://www.mkdocs.org/user-guide/plugins/#on_post_build).

        Rename `index.html` into `covindex.html`.
        Replace every occurrence of `index.html` by `covindex.html` in the HTML files.

        Arguments:
            config: The MkDocs config object.
            kwargs: Additional arguments passed by MkDocs.
        """
        site_coverage_dir = Path(config["site_dir"]) / self.config["page_name"]
        shutil.move(site_coverage_dir / "index.html", site_coverage_dir / "tmp.html")
        try:
            copy_tree(self.config["html_report_dir"], str(site_coverage_dir))
        except DistutilsFileError:
            log.warning("No such HTML report directory: " + self.config["html_report_dir"])
            return
        shutil.move(site_coverage_dir / "index.html", site_coverage_dir / "covindex.html")
        shutil.move(site_coverage_dir / "tmp.html", site_coverage_dir / "index.html")
        for html_file in site_coverage_dir.iterdir():
            if html_file.suffix == ".html" and html_file.name != "index.html":
                html_file.write_text(re.sub(r'href="index\.html"', 'href="covindex.html"', html_file.read_text()))
