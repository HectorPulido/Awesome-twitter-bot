# Generated by Django 3.1.1 on 2021-06-26 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter_data", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="priority",
            field=models.BooleanField(default=False),
        ),
    ]