# Generated by Django 4.0.6 on 2022-08-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_personalinformation_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='haveCasteCertificate',
            field=models.BooleanField(default=False),
        ),
    ]
