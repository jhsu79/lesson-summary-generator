# Generated by Django 4.2.5 on 2023-09-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='program_type',
            field=models.CharField(choices=[('1-on-1', 'O'), ('Small Group', 'S'), ('Classroom', 'C')], max_length=15),
        ),
    ]
