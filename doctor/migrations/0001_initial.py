# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRSTNAME', models.CharField(max_length=40, verbose_name='FIRSTNAME')),
                ('LASTNAME', models.CharField(max_length=40, verbose_name='LASTNAME')),
                ('MIDLLENAME', models.CharField(max_length=40, verbose_name='MIDLLENAME')),
                ('DOB', models.DateField(max_length=8)),
                ('SSN', models.IntegerField(verbose_name=4)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRSTNAME', models.CharField(max_length=40)),
                ('LASTNAME', models.CharField(max_length=40)),
                ('MIDLLENAME', models.CharField(max_length=40)),
                ('DOB', models.DateField(max_length=10, verbose_name='00/00/00')),
                ('SSN', models.IntegerField(verbose_name=4)),
                ('EMAIL', models.CharField(max_length=100, verbose_name='email@email')),
                ('NUMBER', models.IntegerField(max_length=20)),
                ('STREET', models.CharField(max_length=100, verbose_name='street:')),
                ('CITY', models.CharField(max_length=100, verbose_name='city')),
                ('STATE', models.CharField(max_length=2, verbose_name='state:')),
                ('ZIP', models.IntegerField(max_length=5)),
                ('PHONE', models.IntegerField(max_length=10)),
                ('INSURANCE', models.CharField(choices=[('VHCP', 'Veterans Health Care Program'), ('CHAMPVA', 'CHAMPVA'), ('TRICARE', 'TRICARE'), ('NONE', 'NONE')], max_length=50)),
                ('DOCTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
            ],
        ),
    ]