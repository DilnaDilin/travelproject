from django.db import models

# Create your models here.



# Create your models here.
class Destinations(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    address=models.TextField()
    img = models.ImageField(upload_to='pictures',default='path/to/default/image.jpg')

    def __str__(self):
        return self.name