# Generated by Django 3.1.7 on 2021-03-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_delete_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default='None'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default='None'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dor',
            field=models.DateTimeField(default='None'),
        ),
    ]
