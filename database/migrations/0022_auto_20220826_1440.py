# Generated by Django 3.2.15 on 2022-08-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_auto_20220826_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherinfo',
            name='district1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='district2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='district3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
