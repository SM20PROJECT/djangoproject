# Generated by Django 3.0.4 on 2020-03-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickName', models.CharField(max_length=15)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('eMail', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('E', 'Erkek'), ('K', 'Kadın'), ('N', 'Belirmek istemiyorum.')], max_length=20)),
            ],
        ),
    ]
