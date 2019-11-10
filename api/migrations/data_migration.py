from django.db import migrations
from api.models import PizzaFlavor

def insert_pizza_flavors(apps, schema_editor):

    pizza_flavors_to_insert = [
        {
            'name': 'Pepperoni',
            's_size_price': 5,
            'm_size_price': 8,
            'l_size_price': 10
        },
        {
            'name': 'Margarita',
            's_size_price': 3,
            'm_size_price': 5,
            'l_size_price': 8
        },
        {
            'name': 'Neapolitan',
            's_size_price': 7,
            'm_size_price': 9,
            'l_size_price': 11
        }
    ]

    for pizza_flavor_to_insert in pizza_flavors_to_insert:
        PizzaFlavor.objects.create(
            **pizza_flavor_to_insert
        )

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_pizza_flavors),
    ]