# Generated by Django 3.2.12 on 2023-04-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_review_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movies',
            field=models.TextField(blank=True, null=True),
        ),
    ]