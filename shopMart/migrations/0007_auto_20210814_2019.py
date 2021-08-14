# Generated by Django 3.2 on 2021-08-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopMart', '0006_rename_img_product_main_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='main_Image',
            new_name='main_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_Name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='images',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=1, upload_to='myApp/images'),
            preserve_default=False,
        ),
    ]