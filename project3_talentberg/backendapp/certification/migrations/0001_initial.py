# Generated by Django 3.0.7 on 2020-08-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=100)),
                ('atc_code', models.CharField(max_length=100)),
                ('regdate', models.DateField()),
            ],
        ),
    ]
