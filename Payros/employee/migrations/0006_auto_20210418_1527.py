# Generated by Django 3.1.7 on 2021-04-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employee_bank_ac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dor',
            field=models.DateField(auto_now_add=True),
        ),
    ]
