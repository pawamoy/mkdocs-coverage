# MkDocs Coverage Plugin

MkDocs plugin to integrate your coverage HTML report into your site.

## Installation

```
pip install mkdocs-coverage
```

```
python3.8 -m pip install --user pipx
pipx install mkdocs-coverage
```

## Usage

```
# mkdocs.yml
nav:
- Coverage report: coverage.md

plugins:
- coverage:
    page_path: coverage  # default
    html_report_dir: htmlcov  # default
```

The page path can be nested:

```
# mkdocs.yml
nav:
- Coverage report: dev/reports/coverage.md

plugins:
- coverage:
    page_path: dev/reports/coverage
```

If the page doesn't exist, it will be created. If the page exists, the coverage report will be appended at the end. You can choose *where* to insert the coverage report in the page thanks to the `placeholder` setting:

```
# mkdocs.yml
nav:
- Coverage report: dev/coverage.md  # existing page

plugins:
- coverage:
    page_path: dev/coverage
    placeholder: "[INSERT REPORT HERE]"
```

In your page:

```
# Some page

Some text.

## Coverage report

[INSERT REPORT HERE]
```

The plugin will replace any such string with the coverage report. **The default placeholder is `<!-- mkdocs-coverage -->`**.

Now serve your documentation, and go to <http://localhost:8000/coverage/> to see your coverage report!
