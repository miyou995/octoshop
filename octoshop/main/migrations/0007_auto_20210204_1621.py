# Generated by Django 3.1.5 on 2021-02-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210204_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='taille',
            field=models.ManyToManyField(blank=True, null=True, to='main.Taille'),
        ),
    ]
