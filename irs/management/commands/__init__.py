import os
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand


class IRSCommand(BaseCommand):
    """
    Base management command that provides common functionality for the other
    commands in this app.
    """
    url = 'http://forms.irs.gov/app/pod/dataDownload/fullData'

    def handle(self, *args, **options):
        """
        Sets options common to all commands.
        Any command subclassing this object should implement its own
        handle method, as is standard in Django, and run this method
        via a super call to inherit its functionality.
        """

        # Create a data directory
        self.data_dir = os.path.join(
            settings.BASE_DIR,
            'data')
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        # Start the clock
        self.start_datetime = datetime.now()
