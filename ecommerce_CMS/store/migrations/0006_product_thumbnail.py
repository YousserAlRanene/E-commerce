# Generated by Django 5.0.3 on 2024-04-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product_images/thumbnail/'),
        ),
    ]
