from django.db import models

class GLBModel(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='models/')

    def __str__(self):
        return self.name