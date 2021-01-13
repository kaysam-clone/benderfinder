from django.db import models

# Create your models here.


class UserInfo(models.Model):
    full_name = models.CharField(max_length=255)
    bender = models.CharField(max_length=15)
    image = models.ImageField()


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.full_name


class Video(models.Model):
    name = models.CharField(max_length=244, default='bender')
    video = models.FileField()
    def __str__(self):
        return self.name