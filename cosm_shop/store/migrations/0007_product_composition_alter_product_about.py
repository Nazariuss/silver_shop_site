# Generated by Django 4.0.2 on 2022-03-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.TextField(max_length=500, null=True),
        ),
    ]