# Generated by Django 4.1.4 on 2023-03-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0017_alter_extrafield_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="extrafield",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
    ]
