# Generated by Django 4.2.9 on 2024-01-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datainsert',
            name='name',
            field=models.CharField(default='x', max_length=200),
        ),
        migrations.AddField(
            model_name='datainsert',
            name='play',
            field=models.CharField(default='x', max_length=200),
        ),
        migrations.AddField(
            model_name='datainsert',
            name='title',
            field=models.CharField(default='x', max_length=200),
        ),
    ]
