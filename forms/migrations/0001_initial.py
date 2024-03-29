# Generated by Django 3.0.4 on 2020-04-08 16:42

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formTitle', models.CharField(max_length=200)),
                ('formDescription', models.TextField()),
                ('dateOfCreation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionTag', models.CharField(max_length=50)),
                ('typeOfField', models.CharField(max_length=20)),
                ('labelField', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=None, null=True, size=None)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.FormTemplate')),
            ],
        ),
    ]
