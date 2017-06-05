# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_remove_userprofile_location_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Name_logo',
            new_name='category_logo',
        ),
    ]
