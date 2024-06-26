# Generated by Django 5.0.1 on 2024-01-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=150)),
                ('eventdate', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('likes', models.IntegerField(blank=True)),
                ('creator_id', models.IntegerField()),
                ('file_archive', models.FileField(upload_to='')),
                ('password', models.CharField(blank=True, max_length=30)),
                ('unique_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('datejoined', models.DateField(auto_now=True)),
                ('saved_file_archive', models.FileField(blank=True, upload_to='')),
                ('identification_photo_archive', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
