import uuid
from django.db import models

# Create your models here.

class Tracks(models.Model):
    title = models.ForeignKey('Titles', on_delete=models.PROTECT)
    artist = models.ForeignKey('Artists', on_delete=models.PROTECT)
    album = models.ForeignKey('Albums', on_delete=models.PROTECT)
    track_number = models.IntegerField('Номер трека')
    duration = models.IntegerField('Длительность')
    tempo = models.IntegerField('BPM')
    isrc_code = models.CharField('ISRC', max_length=12)
    explict = models.BooleanField('Explict', default=False)
    def __str__(self):
        return str(self.artist) + " - " + str(self.title)
    class Meta:
        verbose_name = 'Track'

class Titles(models.Model):
    title = models.CharField('Название трека', max_length=150)
    title_alt = models.CharField('Альт. название трека', max_length=150, blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Title'

class Artists(models.Model):
    name = models.CharField('Исполнитель', max_length=150)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Artist'

class Albums(models.Model):
    name = models.CharField('Название', max_length=150)
    artist = models.ForeignKey('Artists', on_delete=models.PROTECT)
    release_date = models.DateField('Дата выхода')
    cover_art = models.CharField('Обложка', blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Album'