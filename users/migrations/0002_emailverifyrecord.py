# Generated by Django 2.0 on 2018-01-06 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=10)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
