# Generated by Django 3.1.4 on 2020-12-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercity',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
