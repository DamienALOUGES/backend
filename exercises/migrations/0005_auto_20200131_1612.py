# Generated by Django 3.0 on 2020-01-31 15:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_exercise_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='key_words',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=25), blank=True, null=True, size=10),
        ),
    ]