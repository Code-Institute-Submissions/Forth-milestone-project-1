# Generated by Django 3.1.3 on 2020-11-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='brand',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='category',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='color1',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='color2',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='color3',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='color4',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='name',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='sub_categories',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='url1',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='url2',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='url3',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='url4',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
