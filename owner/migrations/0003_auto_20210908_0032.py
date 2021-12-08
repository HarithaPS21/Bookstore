# Generated by Django 3.2.6 on 2021-09-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_remove_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]