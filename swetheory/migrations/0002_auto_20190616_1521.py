# Generated by Django 2.0.9 on 2019-06-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swetheory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaofinterest',
            name='name',
            field=models.CharField(help_text='Enter area of study', max_length=60),
        ),
    ]