# Generated by Django 3.2.6 on 2022-03-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('rid', models.BigAutoField(primary_key=True, serialize=False)),
                ('roomtype', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('day', models.CharField(max_length=100)),
            ],
        ),
    ]
