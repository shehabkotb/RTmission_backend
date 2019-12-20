# Generated by Django 3.0.1 on 2019-12-20 09:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message="please enter 11 digits in form '01xxxxxxx'", regex='^01\\d{9}$')])),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('comment', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]