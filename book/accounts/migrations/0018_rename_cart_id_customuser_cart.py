# Generated by Django 5.0 on 2023-12-29 18:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0017_remove_customuser_cart_customuser_cart_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="cart_id",
            new_name="cart",
        ),
    ]