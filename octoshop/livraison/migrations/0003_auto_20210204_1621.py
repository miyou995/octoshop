# Generated by Django 3.1.5 on 2021-02-04 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraison', '0002_auto_20210201_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commune',
            old_name='wilaya',
            new_name='Wilaya',
        ),
    ]
