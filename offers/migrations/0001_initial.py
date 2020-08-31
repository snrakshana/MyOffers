# Generated by Django 3.1 on 2020-08-31 08:27

import django.core.validators
from django.db import migrations, models
import offers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OffersAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('category', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to=offers.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_expired', models.DateField(verbose_name='date Expired')),
            ],
        ),
    ]
