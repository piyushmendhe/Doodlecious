# Generated by Django 3.0.8 on 2020-07-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
