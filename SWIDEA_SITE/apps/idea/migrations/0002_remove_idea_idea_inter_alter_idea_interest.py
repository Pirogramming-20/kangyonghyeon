# Generated by Django 5.0.1 on 2024-01-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("idea", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="idea",
            name="idea_inter",
        ),
        migrations.AlterField(
            model_name="idea",
            name="interest",
            field=models.IntegerField(default=0, verbose_name="아이디어 관심도"),
        ),
    ]
