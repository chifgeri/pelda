# Generated by Django 2.1.1 on 2018-09-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korok', '0002_kor_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hallgato',
            name='neptun',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
