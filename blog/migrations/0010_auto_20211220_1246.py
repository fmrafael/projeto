# Generated by Django 3.1.5 on 2021-12-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211217_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableaffiliate',
            name='description_affiliate',
            field=models.CharField(default='Marketing de Afiliados', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tableaffiliate',
            name='category_affiliate',
            field=models.CharField(max_length=200),
        ),
    ]