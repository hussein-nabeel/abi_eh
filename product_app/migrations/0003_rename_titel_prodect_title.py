# Generated by Django 3.2.18 on 2023-03-03 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_alter_prodect_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodect',
            old_name='titel',
            new_name='title',
        ),
    ]
