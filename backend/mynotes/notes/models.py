from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(unique=True, max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title
