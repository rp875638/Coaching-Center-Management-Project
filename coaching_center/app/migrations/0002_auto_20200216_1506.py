# Generated by Django 3.0 on 2020-02-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='idassignment',
            field=models.BooleanField(primary_key=True, serialize=False),
        ),
    ]
