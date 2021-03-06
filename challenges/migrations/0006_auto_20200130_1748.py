# Generated by Django 3.0 on 2020-01-30 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0005_auto_20200129_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challenge_type',
            field=models.IntegerField(choices=[(1, 'Coding Game'), (2, 'Professional'), (3, 'Community')]),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to=settings.AUTH_USER_MODEL),
        ),
    ]
