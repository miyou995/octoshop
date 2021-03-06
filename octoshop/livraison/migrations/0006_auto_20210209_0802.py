# Generated by Django 3.1.5 on 2021-02-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraison', '0005_wilaya_cout'),
    ]

    operations = [
        migrations.AddField(
            model_name='wilaya',
            name='activer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='wilaya',
            name='cout',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='coût de livraison'),
        ),
    ]
