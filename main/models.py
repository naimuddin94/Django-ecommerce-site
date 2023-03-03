from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=200, null=True, blank=True)
    price = models.IntegerField()
    first_star = models.BooleanField(default=False)
    secound_star = models.BooleanField(default=False)
    third_star = models.BooleanField(default=False)
    four_star = models.BooleanField(default=False)
    five_star = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Slider(models.Model):
    image = models.ImageField(upload_to='pics')
    heading = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.heading
    
class About_section(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=700)

    def __str__(self):
        return self.heading
    
class Coustomer(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    comment = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    