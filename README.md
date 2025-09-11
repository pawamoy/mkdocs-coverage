# MkDocs Coverage Plugin

[![ci](https://github.com/pawamoy/mkdocs-coverage/workflows/ci/badge.svg)](https://github.com/pawamoy/mkdocs-coverage/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://pawamoy.github.io/mkdocs-coverage/)
[![pypi version](https://img.shields.io/pypi/v/mkdocs-coverage.svg)](https://pypi.org/project/mkdocs-coverage/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#mkdocs-coverage:gitter.im)

MkDocs plugin to integrate your coverage HTML report into your site.

## Installation

```bash
pip install mkdocs-coverage
```

```bash
python3.8 -m pip install --user pipx
pipx install mkdocs-coverage
```

## Usage

```yaml
# mkdocs.yml
nav:
- Coverage report: coverage.md

plugins:
- coverage:
    page_path: coverage  # default
    html_report_dir: htmlcov  # default
```

The page path can be nested:

```yaml
# mkdocs.yml
nav:
- Coverage report: dev/reports/coverage.md

plugins:
- coverage:
    page_path: dev/reports/coverage
```

If the page doesn't exist, it will be created. If the page exists, the coverage report will be appended at the end.
You can choose *where* to insert the coverage report in the page thanks to the `placeholder` setting:

```yaml
# mkdocs.yml
nav:
- Coverage report: dev/coverage.md  # existing page

plugins:
- coverage:
    page_path: dev/coverage
    placeholder: "[INSERT REPORT HERE]"
```

In your page:

```md
# Some page

Some text.

## Coverage report

[INSERT REPORT HERE]
```

The plugin will replace any such string with the coverage report. **The default placeholder is `<!-- mkdocs-coverage -->`**.

Now serve your documentation,
and go to http://localhost:8000/coverage/
to see your coverage report!

![coverage index](https://user-images.githubusercontent.com/3999221/106802970-f4376a80-6663-11eb-8665-e9e09f0f4ac0.png)
![coverage module](https://user-images.githubusercontent.com/3999221/106803017-fe596900-6663-11eb-9df9-973755c5b63e.png)
