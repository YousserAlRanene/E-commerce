# Generated by Django 5.0.3 on 2024-04-13 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_image_alter_product_thumbnail_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merchant_id',
            new_name='payment_intent',
        ),
    ]
