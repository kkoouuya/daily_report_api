# Generated by Django 3.2.7 on 2021-09-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_daily_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
