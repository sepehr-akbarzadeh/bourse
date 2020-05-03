# Generated by Django 2.2.10 on 2020-05-03 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RemoveField(
            model_name='productpicture',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.ProductPicture', verbose_name='Product Picture'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productlevel',
            name='slug',
            field=models.SlugField(editable=False, max_length=140, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='height_field',
            field=models.SmallIntegerField(editable=False, verbose_name='Height Field'),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='width_field',
            field=models.SmallIntegerField(editable=False, verbose_name='Width Field'),
        ),
    ]