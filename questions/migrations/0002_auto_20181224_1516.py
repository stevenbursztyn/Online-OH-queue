# Generated by Django 2.1.4 on 2018-12-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author_first_name',
            field=models.CharField(default='No first name', max_length=512),
        ),
        migrations.AddField(
            model_name='question',
            name='author_last_name',
            field=models.CharField(default='No last name', max_length=512),
        ),
    ]
