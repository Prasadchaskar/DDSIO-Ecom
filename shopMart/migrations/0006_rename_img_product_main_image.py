# Generated by Django 3.2 on 2021-07-28 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopMart', '0005_auto_20210721_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Img',
            new_name='main_Image',
        ),
    ]
