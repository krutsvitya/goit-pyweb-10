# Generated by Django 5.1.2 on 2024-10-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorsapp', '0003_alter_quote_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
