# Generated by Django 3.2.15 on 2022-08-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20220822_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='casteCertificateimage',
            field=models.ImageField(blank=True, default='', null=True, upload_to='casteCertificateimages/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='safaiKarmchariCertificateimage',
            field=models.ImageField(blank=True, default='', null=True, upload_to='safaiKarmchariCertificateimages/'),
        ),
    ]
