# Generated by Django 4.1.6 on 2023-02-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JohnCarAirCo', '0004_productunit_unitname'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]