# Generated by Django 2.2.7 on 2019-12-22 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_remove_post_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
