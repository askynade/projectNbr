# Generated by Django 3.2.15 on 2022-08-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_rename_havesafaikarmchari_customuser_havesafaikarmchariid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='casteCertificateimage',
            field=models.FileField(blank=True, default='images/No_image_available.png', null=True, upload_to='casteCertificateimages/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='safaiKarmchariCertificateimage',
            field=models.FileField(blank=True, default='images/No_image_available.png', null=True, upload_to='safaiKarmchariCertificateimages/'),
        ),
    ]
