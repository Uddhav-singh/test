# Generated by Django 4.2.4 on 2023-08-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "scheduling",
            "0003_alter_instructor_options_alter_instructor_managers_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="lecture",
            name="name",
            field=models.CharField(default="Lecture name", max_length=200),
        ),
    ]