# Generated by Django 3.1.3 on 2020-12-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201207_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='website',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
