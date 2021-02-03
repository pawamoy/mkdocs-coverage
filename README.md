# MkDocs Coverage Plugin

[![ci](https://github.com/pawamoy/mkdocs-coverage/workflows/ci/badge.svg)](https://github.com/pawamoy/mkdocs-coverage/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pawamoy.github.io/mkdocs-coverage/)
[![pypi version](https://img.shields.io/pypi/v/mkdocs-coverage.svg)](https://pypi.org/project/mkdocs-coverage/)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/mkdocs-coverage/community)

MkDocs plugin to integrate your coverage HTML report into your site.

## Requirements

MkDocs Coverage Plugin requires Python 3.6 or above.

<details>
<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.6
pyenv install 3.6.12

# make it available globally
pyenv global system 3.6.12
```
</details>

## Installation

With `pip`:
```bash
python3.6 -m pip install mkdocs-coverage
```

With [`pipx`](https://github.com/pipxproject/pipx):
```bash
python3.6 -m pip install --user pipx

pipx install --python python3.6 mkdocs-coverage
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
