# Generated by Django 3.1.5 on 2021-12-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20211207_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo_body1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_body2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_body3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_title',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]