from django.db import models

class Bild(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=1024)
    description = models.TextField()

    def __str__(self):
        return self.name
