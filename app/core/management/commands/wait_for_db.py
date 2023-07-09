"""
DJANGO command to wait for the database to be available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ DJANGO commando to wait for db """

    def handle(self, *args, **options):
        pass