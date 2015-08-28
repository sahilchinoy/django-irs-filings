import os
import math
import csv
import string
import shutil
import requests
import zipfile
from datetime import datetime
import boto
from filechunkio import FileChunkIO
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
        self.final_path = os.path.join(
            settings.DATA_DIR,
            'FullDataFile-{}.txt'.format(self.current_date))

        #self.download()
        #self.unzip()
        #self.clean()

        c = boto.s3.connect_to_region('us-west-1')
        b = c.get_bucket('irs-itemizer')

        # Get file info
        source_path = self.final_path
        source_size = os.stat(source_path).st_size

        # Create a multipart upload request
        mp = b.initiate_multipart_upload(os.path.basename(source_path))

        # Use a chunk size of 50 MiB (feel free to change this)
        chunk_size = 52428800
        chunk_count = int(math.ceil(source_size / float(chunk_size)))

        # Send the file parts, using FileChunkIO to create a file-like object
        # that points to a certain byte range within the original file. We
        # set bytes to never exceed the original file size.
        for i in range(chunk_count):
            offset = chunk_size * i
            bytes = min(chunk_size, source_size - offset)
            with FileChunkIO(source_path, 'r', offset=offset,bytes=bytes) as fp:
                mp.upload_part_from_file(fp, part_num=i + 1)

        # Finish the upload
        mp.complete_upload()

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
            self.final_path
        )

        #shutil.rmtree(os.path.join(settings.DATA_DIR, 'var'))
        #os.remove(self.zip_path)

