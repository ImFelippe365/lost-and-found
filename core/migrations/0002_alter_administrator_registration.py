# Generated by Django 4.1.3 on 2022-12-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='registration',
            field=models.CharField(max_length=40),
        ),
    ]