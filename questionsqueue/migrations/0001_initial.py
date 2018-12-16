# Generated by Django 2.1.4 on 2018-12-16 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=280)),
                ('ask_date', models.DateTimeField(auto_now_add=True)),
                ('answered_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='TA', to=settings.AUTH_USER_MODEL)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
