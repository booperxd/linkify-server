# Generated by Django 4.2 on 2023-04-24 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkifyapp", "0002_user_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="token",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
