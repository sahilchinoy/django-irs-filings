from irs.management.commands import IRSCommand
from django.core.management import call_command


class Command(IRSCommand):

    help = "Download the latest IRS filings and load them into the database"

    def handle(self, *args, **options):
        call_command('downloadIRS')
        call_command('loadIRS')
