# django-irs
A Django project for downloading, parsing and browsing IRS campaign finance data.

# Background
What is a 527

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


# Downloading
To get started, call the `load` command. This will download the latest zipped archive from the IRS website, unzip and parse it, and insert it into the database.

```bash
$ python manage.py load
```
