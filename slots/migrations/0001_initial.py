# Generated by Django 3.1.3 on 2020-11-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('rest_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('slot_number', models.IntegerField()),
                ('table_no', models.IntegerField()),
            ],
        ),
    ]
