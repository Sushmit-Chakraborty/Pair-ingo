# Generated by Django 4.2.10 on 2024-04-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userAuth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="technology",
            name="technology",
            field=models.CharField(max_length=100, null=True),
        ),
    ]