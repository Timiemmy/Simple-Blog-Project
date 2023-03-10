# Generated by Django 4.1.7 on 2023-03-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("DF", "Draft"), ("PB", "Published")],
                default="DF",
                max_length=2,
            ),
        ),
    ]
