# Generated by Django 3.0 on 2020-01-27 01:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('key_words', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=25), size=10)),
                ('file', models.FileField(blank=True, null=True, upload_to='corrections/%Y/%m/$D/')),
            ],
        ),
    ]
