# Generated by Django 2.1.7 on 2019-05-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190416_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_image',
            field=models.ImageField(default=1, upload_to='pet-pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='', upload_to='profile-pics'),
            preserve_default=False,
        ),
    ]
