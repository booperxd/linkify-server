# Generated by Django 4.2 on 2023-04-24 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkifyapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]