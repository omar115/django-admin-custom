# Generated by Django 3.2.8 on 2021-10-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
