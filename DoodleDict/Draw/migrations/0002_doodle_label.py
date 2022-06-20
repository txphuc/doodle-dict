# Generated by Django 3.1.2 on 2021-12-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Draw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doodle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=256, null=True)),
                ('base64', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_en', models.CharField(max_length=512, null=True)),
                ('word', models.JSONField(blank=True, default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]