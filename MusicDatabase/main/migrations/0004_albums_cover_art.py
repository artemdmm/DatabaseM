# Generated by Django 4.2 on 2023-04-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_albums_performer_albums_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='cover_art',
            field=models.CharField(blank=True, null=True, verbose_name='Обложка'),
        ),
    ]