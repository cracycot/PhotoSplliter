# Generated by Django 5.0.1 on 2024-01-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_alter_users_saved_file_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersIdentificationphotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_photo_archive', models.FileField(upload_to='uploads_files')),
            ],
        ),
        migrations.CreateModel(
            name='UsersSavedArchives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_file_archive', models.FileField(upload_to='uploads_files')),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='identification_photo_archive',
        ),
        migrations.RemoveField(
            model_name='users',
            name='saved_file_archive',
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
