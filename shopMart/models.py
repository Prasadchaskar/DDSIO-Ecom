from django.db import models
import datetime
# Create your models here.
class Categrory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return  self.name

class Product(models.Model):
    product_Name        = models.CharField(max_length=100)
    price               = models.IntegerField()
    category            = models.ForeignKey(Categrory,on_delete=models.CASCADE)
    color               = models.ForeignKey(Color,on_delete=models.CASCADE)
    short_decription    = models.CharField(max_length=600)
    decription          = models.TextField()
    main_Img            = models.ImageField(upload_to="myApp/images",default="")
    img1                = models.ImageField(upload_to="myApp/images",default="")
    img2                = models.ImageField(upload_to="myApp/images",default="")
    img3                = models.ImageField(upload_to="myApp/images",default="")
    img4                = models.ImageField(upload_to="myApp/images",default="")
    is_available        = models.BooleanField(default=True)
    is_active           = models.BooleanField(default=True)
    created             = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product_Name
