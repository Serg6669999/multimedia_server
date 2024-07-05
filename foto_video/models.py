from django.db import models


class Multimedia(models.Model):
    name = models.CharField(max_length=30, blank=True)
    size = models.IntegerField(blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Foto(Multimedia):
    FILE_TYPE = {
        "jpg": "jpg",
        "jpeg": "jpeg",
        "gif": "gif",
    }
    type = models.CharField(max_length=5, choices=FILE_TYPE, blank=True)
    file = models.FileField(upload_to='foto/', blank=False)


class Video(Multimedia):
    FILE_TYPE = {
        "avi": "avi",
        "mpeg": "mpeg",
        "wmv": "gif",
        "mp4": "mp4"
    }
    type = models.CharField(max_length=5, choices=FILE_TYPE)
    file = models.FileField(upload_to='video/', blank=False)
