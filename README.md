# django-irs
A Django project for downloading and parsing IRS campaign finance data, inspired by the [New York Times Fech library](https://github.com/NYTimes/Fech).

Background
---------------
Some political committees report their contributions and expenditures to the IRS under § 527 of the U.S. tax code. The IRS publishes these disclosure forms as a bulk download. This app attempts to make sense of that bulk export.

The [archive](http://forms.irs.gov/app/pod/dataDownload/dataDownload) is updated every Sunday at 1:00 AM. 

Getting started
---------------

Install `django-irs-filings` as an app in a Django project.

```bash
$ pip install django-irs-filings
```

To get started, call the `load` command. This will download the latest zipped archive from the IRS website, unzip and parse it, and insert it into the database.

```bash
$ python manage.py load
```