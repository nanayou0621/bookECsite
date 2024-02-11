# Generated by Django 5.0 on 2023-12-27 05:14

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_customuser_is_received_email"),
        ("books", "0004_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "purchase_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="購入時刻"
                    ),
                ),
                (
                    "perchase_num",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(10)],
                        verbose_name="購入数",
                    ),
                ),
                ("state_flag", models.BooleanField(default=True, verbose_name="運用状況")),
                (
                    "fk_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="books.book",
                        verbose_name="書籍",
                    ),
                ),
                (
                    "fk_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="ユーザー",
                    ),
                ),
            ],
        ),
    ]
