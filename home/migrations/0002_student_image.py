# Generated by Django 5.0 on 2023-12-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="image",
            field=models.ImageField(
                default="default_image.jpg", upload_to="student_images/"
            ),
        ),
    ]