# Generated by Django 5.0 on 2023-12-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='お問合せ日時')),
                ('content', models.TextField(verbose_name='お問合せ内容')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('fullname', models.CharField(max_length=30, verbose_name='氏名')),
                ('kana', models.CharField(max_length=60, verbose_name='フリガナ')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
