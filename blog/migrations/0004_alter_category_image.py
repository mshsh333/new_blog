# Generated by Django 4.2.7 on 2023-11-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='post_image/', verbose_name='Картинка'),
        ),
    ]
