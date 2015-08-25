import os
import csv
import string
import shutil
import requests
import zipfile
from datetime import datetime
from dateutil.parser import parse as dateparse
from django.conf import settings
from django.core.management.base import BaseCommand

from irs.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.url = 'http://forms.irs.gov/app/pod/dataDownload/fullData'
        self.zip_path = os.path.join(settings.DATA_DIR,'zipped_archive.zip')
        self.extract_path = os.path.join(settings.DATA_DIR)
        self.current_date = datetime.strftime(datetime.now(),'%m%d%y')

        self.download()
        self.unzip()
        self.clean()

    def download(self): 
        print 'Starting download'
        r = requests.get(self.url, stream=True)
        with open(self.zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=4096):
                print 'Downloading...'
                f.write(chunk)
                f.flush()

    def unzip(self):
        print 'Unzipping archive'
        with zipfile.ZipFile(self.zip_path,'r') as zipped_archive:
            data_file =  zipped_archive.namelist()[0]
            zipped_archive.extract(data_file, self.extract_path)

    def clean(self):
        print 'Cleaning up archive'
        shutil.move(
            os.path.join(
                settings.DATA_DIR,
                'var/IRS/data/scripts/pofd/download/FullDataFile.txt'
            ),
            os.path.join(settings.DATA_DIR, 'FullDataFile-{}.txt'.format(self.current_date))
        )

        shutil.rmtree(os.path.join(settings.DATA_DIR, 'var'))
        os.remove(self.zip_path)

