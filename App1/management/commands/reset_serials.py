from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset the serial numbers of all tables'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            # Replace 'App1_caritem' with your actual table name
            cursor.execute("DELETE FROM App1_caritem")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='App1_caritem'")
            self.stdout.write(self.style.SUCCESS('Successfully reset serial numbers.'))
