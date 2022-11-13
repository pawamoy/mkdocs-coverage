# MkDocs Coverage Plugin

[![ci](https://github.com/pawamoy/mkdocs-coverage/workflows/ci/badge.svg)](https://github.com/pawamoy/mkdocs-coverage/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pawamoy.github.io/mkdocs-coverage/)
[![pypi version](https://img.shields.io/pypi/v/mkdocs-coverage.svg)](https://pypi.org/project/mkdocs-coverage/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/pawamoy/mkdocs-coverage)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/mkdocs-coverage/community)

MkDocs plugin to integrate your coverage HTML report into your site.

## Installation

With `pip`:
```bash
pip install mkdocs-coverage
```

With [`pipx`](https://github.com/pipxproject/pipx):
```bash
python3.7 -m pip install --user pipx
pipx install mkdocs-coverage
```

## Usage

```yaml
# mkdocs.yml

nav:
- Coverage report: coverage.md

plugins:
- coverage:
    page_name: coverage  # default
    html_report_dir: htmlcov  # default
```

Now serve your documentation,
and go to http://localhost:8000/coverage/
to see your coverage report!

![coverage index](https://user-images.githubusercontent.com/3999221/106802970-f4376a80-6663-11eb-8665-e9e09f0f4ac0.png)
![coverage module](https://user-images.githubusercontent.com/3999221/106803017-fe596900-6663-11eb-9df9-973755c5b63e.png)
