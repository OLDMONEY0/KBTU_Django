# Generated by Django 4.1.13 on 2024-05-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="photo",
            field=models.ImageField(
                blank=True, default="assets/dog.jpeg", null=True, upload_to="users"
            ),
        ),
    ]
