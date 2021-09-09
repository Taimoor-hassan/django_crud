from django.db import models

# Create your models here.
class student (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    