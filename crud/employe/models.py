from django.db import models

# Create your models here.

class employe(models.Model):
    NAME = models.CharField(max_length=300)
    ADDRESS = models.TextField(max_length=300)
    NUMBER = models.IntegerField()
    EMAIL = models.EmailField()
    Idno = models.IntegerField(default=0)

    def __str__(self):
        return self.NAME
    