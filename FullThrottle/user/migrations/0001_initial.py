# Generated by Django 2.2.7 on 2020-06-24 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.CharField(max_length=10)),
                ('endDate', models.CharField(max_length=10)),
                ('startTime', models.CharField(max_length=15)),
                ('endTime', models.CharField(max_length=15)),
                ('id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Member')),
            ],
        ),
    ]