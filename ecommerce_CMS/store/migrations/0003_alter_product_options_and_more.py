# Generated by Django 5.0.3 on 2024-04-02 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descripton',
            new_name='description',
        ),
    ]
