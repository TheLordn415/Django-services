from django.db import models
# Create your models here.
class InputFile(models.Model):
    file = models.FileField(upload_to='')