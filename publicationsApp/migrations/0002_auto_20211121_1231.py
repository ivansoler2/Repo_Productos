# Generated by Django 3.2.7 on 2021-11-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicationsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(upload_to='app/category/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(upload_to='app/publications/'),
        ),
    ]
