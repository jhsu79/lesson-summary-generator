# Generated by Django 4.2.5 on 2023-09-26 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_student_pronouns_alter_student_program_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Lesson Date')),
                ('homework_notes', models.CharField(max_length=100)),
                ('lesson_comments', models.CharField(max_length=200)),
                ('homework_assigned', models.BooleanField(default=True)),
                ('assigned_homework', models.TextField(max_length=250)),
                ('next_lesson_date', models.DateField(verbose_name='Next Lesson Date')),
                ('private_notes', models.TextField()),
                ('concepts_covered', models.ManyToManyField(blank=True, to='main_app.concept')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.student')),
            ],
        ),
    ]
