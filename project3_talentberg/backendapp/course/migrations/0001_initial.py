# Generated by Django 3.0.7 on 2020-08-02 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.TextField(max_length=100)),
                ('duration', models.IntegerField()),
                ('fees', models.FloatField()),
                ('course_content', models.FileField(upload_to='syllabus/')),
                ('fkcertificateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.Certificate')),
                ('fkcourseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]
