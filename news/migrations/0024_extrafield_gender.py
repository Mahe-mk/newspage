# Generated by Django 4.1.4 on 2023-03-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0023_remove_extrafield_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="extrafield",
            name="gender",
            field=models.TextField(blank=True, null=True),
        ),
    ]