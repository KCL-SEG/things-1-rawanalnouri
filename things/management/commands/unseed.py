from django.core.management.base import BaseCommand, CommandError
from things.models import Thing

class Command(BaseCommand):
    help = "Unseeds the database."

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        deleted_things = Thing.objects.all().count()
        Thing.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Number of deleted things: {deleted_things}"))