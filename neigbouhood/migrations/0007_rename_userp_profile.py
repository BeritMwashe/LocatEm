# Generated by Django 3.2.7 on 2021-09-25 09:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neigbouhood', '0006_bussinessclass_bimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserP',
            new_name='Profile',
        ),
    ]