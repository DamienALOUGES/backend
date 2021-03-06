# Generated by Django 3.0 on 2020-01-27 13:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20200127_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='corrections/%Y/%m/$D/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'tex', 'py', 'r'])]),
        ),
    ]
