# Generated by Django 3.1.7 on 2021-04-21 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20210421_1314'),
        ('bankadvice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankadvice',
            name='emp_name',
        ),
        migrations.AlterField(
            model_name='bankadvice',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.qualification'),
        ),
    ]
