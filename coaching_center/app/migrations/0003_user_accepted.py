# Generated by Django 3.0 on 2020-02-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200216_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted',
            field=models.IntegerField(blank=True, default=False, null=True),
        ),
    ]
