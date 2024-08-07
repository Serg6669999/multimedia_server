# Generated by Django 5.0.6 on 2024-07-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('jpg', 'jpg'), ('jpeg', 'jpeg'), ('gif', 'gif')], max_length=5)),
                ('file', models.FileField(upload_to='foto/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('avi', 'avi'), ('mpeg', 'mpeg'), ('wmv', 'gif')], max_length=5)),
                ('file', models.FileField(upload_to='video/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
