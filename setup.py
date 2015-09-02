import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-irs-filings',
    version='0.1',
    packages=['irs'],
    include_package_data=True,
    license='MIT',
    description='A Django app to download IRS 527 filings and \
    load them into a database',
    long_description=README,
    url='https://github.com/sahilchinoy/django-irs',
    author='Sahil Chinoy',
    author_email='sahil.chinoy@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires = [
        'probablepeople>=0.3.1',
        'requests>=2.7.0',
    ]
)