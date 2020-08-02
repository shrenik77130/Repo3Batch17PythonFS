# Generated by Django 3.0.7 on 2020-08-02 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enqdate', models.DateField()),
                ('batchtime', models.CharField(max_length=100)),
                ('remark', models.TextField()),
                ('fkcourseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseMaster')),
                ('fkstatusid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiry.Status')),
                ('fkstudid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
