import os
from setuptools import setup
from distutils.core import Command

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS=('irs',)
        )
        from django.core.management import call_command
        from django.conf import settings
        import django
        if django.VERSION[:2] >= (1, 7):
            django.setup()
            settings.BASE_DIR = os.path.dirname(__file__)
        call_command('test', 'irs')

setup(
    name='django-irs-filings',
    version='0.1.5',
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        'requests>=2.7.0',
    ],
    cmdclass={
        'test': TestCommand
    },
)
