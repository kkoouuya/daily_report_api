# Generated by Django 3.2.7 on 2021-09-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210927_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
