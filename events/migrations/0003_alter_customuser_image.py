# Generated by Django 4.0.1 on 2022-01-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_customuser_image_customuser_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/media'),
        ),
    ]