# Generated by Django 2.1.4 on 2019-01-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohqueue', '0012_merge_20190107_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='ohqueue',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
