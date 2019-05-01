from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    Date = models.DateTimeField()
    Body = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')
    def summary(self):
        return self.Body[:300]

    def __str__(self):
        return self.title
    
    
    