# Generated by Django 2.1.1 on 2018-09-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korok', '0003_auto_20180922_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hallgato',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='hallgato',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]