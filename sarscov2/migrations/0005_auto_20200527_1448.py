# Generated by Django 3.0.6 on 2020-05-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sarscov2", "0004_delete_coronakapinformationsources"),
    ]

    operations = [
        migrations.AddField(
            model_name="coronaviruskap",
            name="collection_method",
            field=models.CharField(
                choices=[
                    ("in_person", "In person"),
                    ("remote", "Remotely, by telephone"),
                ],
                default="in_person",
                max_length=25,
                verbose_name="How was this information collected?",
            ),
        ),
        migrations.AddField(
            model_name="historicalcoronaviruskap",
            name="collection_method",
            field=models.CharField(
                choices=[
                    ("in_person", "In person"),
                    ("remote", "Remotely, by telephone"),
                ],
                default="in_person",
                max_length=25,
                verbose_name="How was this information collected?",
            ),
        ),
        migrations.AlterField(
            model_name="coronaviruskap",
            name="protocol",
            field=models.CharField(default="sarscov2", max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalcoronaviruskap",
            name="protocol",
            field=models.CharField(default="sarscov2", max_length=50),
        ),
    ]
