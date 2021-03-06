# Generated by Django 3.0.7 on 2020-08-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('suburb', models.TextField(max_length=100)),
                ('city', models.TextField(max_length=100)),
                ('pincode', models.TextField(max_length=100)),
                ('whatsappno', models.TextField(max_length=100)),
                ('parentsno', models.TextField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
            ],
        ),
    ]
