# Generated by Django 4.0 on 2023-02-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchmate_app', '0003_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='website',
            field=models.URLField(max_length=100),
        ),
    ]
