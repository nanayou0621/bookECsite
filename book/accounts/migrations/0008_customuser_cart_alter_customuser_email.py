# Generated by Django 5.0 on 2023-12-27 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_purchase"),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="cart",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.cart",
                verbose_name="カート",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=64, unique=True, verbose_name="メールアドレス"),
        ),
    ]
