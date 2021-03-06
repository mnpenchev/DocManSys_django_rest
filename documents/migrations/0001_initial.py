# Generated by Django 3.1 on 2020-11-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=2000)),
                ('date', models.DateField()),
                ('signed', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
