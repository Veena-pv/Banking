# Generated by Django 4.1.4 on 2022-12-09 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='country',
            new_name='district',
        ),
    ]
