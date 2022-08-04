# Generated by Django 4.0.6 on 2022-08-01 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_customuser_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherinfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CustomUserOtherInfo', to=settings.AUTH_USER_MODEL),
        ),
    ]
