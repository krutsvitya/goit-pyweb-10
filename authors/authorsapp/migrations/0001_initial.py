# Generated by Django 5.1.2 on 2024-10-29 19:51

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('born_date', models.CharField(blank=True, max_length=100, null=True)),
                ('born_location', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), default=list, size=None)),
                ('quote', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='authorsapp.author')),
            ],
        ),
    ]