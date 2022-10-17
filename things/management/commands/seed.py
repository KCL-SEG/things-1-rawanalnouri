from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from things.models import Thing
import faker.providers
import random

THINGS = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Hairbrush",
    "Jeans",
    "Ties",
    "PrintedShirts",
    "PoloShirt",
    "Concealer",
    "Lipstick",
    "FaceCream",
    "HandCream",
    "Mascara",
    "DIYToolset",
    "Hammer",
    "GlueGun",
    "LightBulb",
    "Apple",
    "Potato",
    "Beef",
    "Chicken",
]

class Thing_Provider(faker.providers.BaseProvider):
    def things(self):
        return self.random_element(THINGS)

class Command(BaseCommand):
    help = "Seeds the database for testing and development."

    def __init__(self):
        super().__init__()
        self.fake = Faker('en_GB')
        self.fake.add_provider(Thing_Provider)
    
    def add_arguments(self, parser):
        parser.add_argument('--things',
        default=15,
        type=int,
        help='The number of fake things to create.')

    def handle(self, *args, **options):
        for _ in range(options['things']):
            self.seed()
        check_thing = Thing.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of things: {check_thing}"))
    
    def seed(self):
        name = self.fake.unique.things()
        quantity = random.randint(0,100)
        description = self.fake.paragraph(nb_sentences=2)
        #new entry
        thing = Thing.objects.create(name = name, description = description, quantity = quantity)