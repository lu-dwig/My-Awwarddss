# Generated by Django 4.0.5 on 2022-06-14 07:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0004_rename_author_post_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rating',
            new_name='Ratings',
        ),
    ]
