# Generated by Django 5.1.1 on 2024-10-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoryapp', '0002_datafortablemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafortablemodel',
            name='category',
            field=models.CharField(default='test', max_length=200),
        ),
        migrations.AddField(
            model_name='sidebarmenumodel',
            name='category',
            field=models.CharField(default='test', max_length=200),
        ),
    ]
