import os
import shutil
import zipfile
import logging
import requests
from irs.management.commands import IRSCommand

logger = logging.getLogger(__name__)


class Command(IRSCommand):
    help = "Download the latest IRS archive"

    def add_arguments(self, parser):
        parser.add_argument(
            '--test',
            action='store_true',
            dest='test',
            default=False,
            help='Use a subset of data for testing',
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            dest='verbose',
            default=False,
            help='More logging messages',
        )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        # Configure the logger
        FORMAT = '%(asctime)s %(levelname)s: %(message)s'
        if options['verbose']:
            logging.basicConfig(
                format=FORMAT,
                datefmt='%I:%M:%S',
                level=logging.DEBUG)
        else:
            logging.basicConfig(
                format=FORMAT,
                datefmt='%I:%M:%S',
                level=logging.INFO)

        # Where to download the raw zipped archive
        self.zip_path = os.path.join(
            self.data_dir,
            'zipped_archive.zip')
        # Where to extract the archive
        self.extract_path = os.path.join(
            self.data_dir)
        # Where to store the data file
        self.final_path = os.path.join(
            self.data_dir,
            'FullDataFile.txt')

        logger.info('Downloading latest archive')
        self.download()
        self.unzip()
        self.clean()

    def download(self):
        """
        Download the archive from the IRS website.
        """
        url = 'http://forms.irs.gov/app/pod/dataDownload/fullData'
        r = requests.get(url, stream=True)
        with open(self.zip_path, 'wb') as f:
            # This is a big file, so we download in chunks
            for chunk in r.iter_content(chunk_size=30720):
                logger.debug('Downloading...')
                f.write(chunk)
                f.flush()

    def unzip(self):
        """
        Unzip the archive.
        """
        logger.info('Unzipping archive')
        with zipfile.ZipFile(self.zip_path, 'r') as zipped_archive:
            data_file = zipped_archive.namelist()[0]
            zipped_archive.extract(data_file, self.extract_path)

    def clean(self):
        """
        Get the .txt file from within the many-layered
        directory structure, then delete the directories.
        """
        logger.info('Cleaning up archive')
        shutil.move(
            os.path.join(
                self.data_dir,
                'var/IRS/data/scripts/pofd/download/FullDataFile.txt'
            ),
            self.final_path
        )

        shutil.rmtree(os.path.join(self.data_dir, 'var'))
        os.remove(self.zip_path)
