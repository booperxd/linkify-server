# Generated by Django 4.2 on 2023-04-19 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkifyapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
