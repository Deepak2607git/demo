# Generated by Django 2.2.7 on 2022-04-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
