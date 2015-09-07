A Django app for downloading and parsing IRS campaign finance data, inspired by the [New York Times Fech library](https://github.com/NYTimes/Fech).

[![PyPI version](https://badge.fury.io/py/django-irs-filings.svg)](http://badge.fury.io/py/django-irs-filings)
[![Build Status](https://travis-ci.org/sahilchinoy/django-irs-filings.svg?branch=master)](https://travis-ci.org/sahilchinoy/django-irs-filings)

Background
---------------
Some political committees report their contributions and expenditures to the IRS under § 527 of the U.S. tax code. The IRS publishes these disclosure forms as a bulk download. This app attempts to make sense of that bulk export.

The [archive](http://forms.irs.gov/app/pod/dataDownload/dataDownload) is updated every Sunday at 1:00 AM. 

Getting started
---------------

Install it.

```bash
$ pip install django-irs-filings
```

Add `irs` to your list of `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = (
    ...
    'irs',
    ...
)
```

Migrate your database.

```bash
$ python manage.py migrate
```

Finally, call the `load` command. This will download the latest zipped archive from the IRS website, unzip and parse it, and insert it into the database.

```bash
$ python manage.py load
```

Some options for `load`:

Option name | Description
----------- | -----------
`--people` | Uses [probablepeople](https://github.com/datamade/probablepeople) for name parsing
`--test` | Uses a small subset of real data for testing
`--backup` | Loads from an [outdated backup file](https://s3-us-west-1.amazonaws.com/irs-itemizer/FullDataFile.txt)
`--verbose` | Logs filing numbers being parsed to the console
