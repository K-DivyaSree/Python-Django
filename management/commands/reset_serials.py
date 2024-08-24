from django.core.management.base import BaseCommand
from your_app.models import YourModel
from django.db import connection

class Command(BaseCommand):
    help = 'Reset serial numbers in the database'

    def handle(self, *args, **kwargs):
        # Delete existing records
        YourModel.objects.all().delete()

        # Reset auto-increment
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE your_table_name AUTO_INCREMENT = 1;")
        
        # Re-assign serial numbers if needed
        all_objects = YourModel.objects.all().order_by('some_field')
        for index, obj in enumerate(all_objects, start=1):
            obj.serial_no = index
            obj.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully reset serial numbers'))
