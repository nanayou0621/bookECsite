# Generated by Django 5.0 on 2023-12-29 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0011_alter_customuser_managers"),
        ("store", "0002_alter_cartunit_book_alter_cartunit_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="cart",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.cart",
                verbose_name="カート",
            ),
        ),
    ]