# Generated by Django 4.1.3 on 2022-11-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVEmp', '0004_alter_employee_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]