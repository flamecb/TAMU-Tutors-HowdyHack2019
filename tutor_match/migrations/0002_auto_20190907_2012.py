# Generated by Django 2.2.5 on 2019-09-08 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='classID',
            field=models.CharField(max_length=128, verbose_name='Class ID'),
        ),
    ]
