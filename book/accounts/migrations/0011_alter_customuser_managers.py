# Generated by Django 5.0 on 2023-12-29 16:29

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_alter_customuser_cart"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", accounts.models.CustomUserManager()),
            ],
        ),
    ]
