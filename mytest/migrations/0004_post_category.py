# Generated by Django 4.2.4 on 2023-12-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(null=True),
        ),
    ]
