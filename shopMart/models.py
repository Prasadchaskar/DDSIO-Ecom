from django.db import models

# Create your models here.
class Categrory(models.Model):
    category_Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category_Name

class thredType(models.Model):
    thred_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.thred_type

class Color(models.Model):
    color_Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return  self.color_Name
class Material(models.Model):
    material_Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.material_Name

class Shape(models.Model):
    shape_Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.shape_Name

class Product(models.Model):
    product_Name        = models.CharField(max_length=100)
    price               = models.IntegerField()
    category            = models.ForeignKey(Categrory,on_delete=models.CASCADE)
    material            = models.ForeignKey(Material,on_delete=models.CASCADE)
    shape               = models.ForeignKey(Shape,on_delete=models.CASCADE)
    color               = models.ForeignKey(Color,on_delete=models.CASCADE)
    weight              = models.CharField(max_length=50)
    dimensions          = models.CharField(max_length=50)
    thread_Type         = models.ForeignKey(thredType,on_delete=models.CASCADE)
    age_Group           = models.CharField(max_length=100)
    decription          = models.TextField()
    main_Img            = models.ImageField(upload_to="myApp/images",default="")
    img1                = models.ImageField(upload_to="myApp/images",default="")
    img2                = models.ImageField(upload_to="myApp/images",default="")
    img3                = models.ImageField(upload_to="myApp/images",default="")
    img4                = models.ImageField(upload_to="myApp/images",default="")
    def __str__(self) -> str:
        return self.product_Name
