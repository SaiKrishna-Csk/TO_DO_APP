# Generated by Django 2.1.7 on 2019-03-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20190307_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='date',
            field=models.CharField(default='11/11/11', max_length=264),
        ),
        migrations.AddField(
            model_name='list',
            name='time',
            field=models.CharField(default='12:12', max_length=264),
        ),
    ]
