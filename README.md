# django-irs
A Django project for downloading, parsing and browsing IRS campaign finance data, inspired heavily by ProPublica's [FEC Itemizer](https://projects.propublica.org/itemizer/) and the [New York Times Fech library](https://github.com/NYTimes/Fech).

# Background
Some political committees report their contributions and expenditures to the IRS under § 527 of the U.S. tax code. The IRS publishes these disclosure forms as a bulk download. This app attempts to make sense of that bulk export, providing an interface to dissect individual filings and link to contributions and expenditures.

The [archive](http://forms.irs.gov/app/pod/dataDownload/dataDownload) is updated every Sunday at 1:00 AM. 

Getting started
---------------

Requirements:

* Python
* PostgreSQL
* virtualenv
* Git

Create a virtualenv to store the codebase.

```bash
$ virtualenv django-irs
```

Activate the virtualenv.

```bash
$ cd django-irs
$ . bin/activate
```

Clone the git repository from GitHub.

```bash
$ git clone git@github.com:sahilchinoy/django-irs.git repo
```

Enter the project and install its dependencies.

```bash
$ cd repo
$ pip install -r requirements.txt
```

Create a new database for this project.

```bash
$ createdb irs
```

Make a copy of settings_dev.py and configure it to connect to your new database.

```bash
$ cp project/settings_dev.py.template project/settings_dev.py
$ vim project/settings_dev.py
```

Run the test server for the first time. There shouldn't be any filings loaded yet.

```bash
$ python manage.py runserver
```

# Downloading
To get started, call the `load` command. This will download the latest zipped archive from the IRS website, unzip and parse it, and insert it into the database.

```bash
$ python manage.py load
```
