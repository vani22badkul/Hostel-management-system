# Generated by Django 3.1.4 on 2020-12-08 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('hostel_no', models.IntegerField(primary_key=True, serialize=False)),
                ('no_of_rooms', models.IntegerField()),
                ('no_of_students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('room_capacity', models.IntegerField()),
                ('r_hostelno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=70)),
                ('s_fathername', models.CharField(max_length=70)),
                ('s_department', models.CharField(max_length=70)),
                ('s_hostelno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.hostel')),
                ('s_roomno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.room')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_sem', models.IntegerField()),
                ('fee_status', models.CharField(max_length=10)),
                ('s_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]
