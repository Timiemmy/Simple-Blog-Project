# Generated by Django 4.1.7 on 2023-03-02 07:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_slug_alter_post_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
