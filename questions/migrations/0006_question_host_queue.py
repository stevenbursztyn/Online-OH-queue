# Generated by Django 2.1.4 on 2019-01-07 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20190107_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='host_queue',
            field=models.CharField(default='', max_length=32),
        ),
    ]
