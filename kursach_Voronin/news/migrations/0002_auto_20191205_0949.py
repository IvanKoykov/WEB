# Generated by Django 2.2.7 on 2019-12-05 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user',
            new_name='email',
        ),
    ]
