# Generated by Django 3.0 on 2020-01-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_remove_challenge_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='allocated_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='ending_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='language',
            field=models.IntegerField(choices=[(13, 'Python'), (14, 'R')], max_length=50),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='starting_date',
            field=models.DateField(blank=True),
        ),
    ]
