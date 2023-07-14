# Generated by Django 4.2.3 on 2023-07-14 15:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('isbn', models.CharField(max_length=13, unique=True, validators=[django.core.validators.MinLengthValidator(13)])),
                ('genre', models.CharField()),
                ('library_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.library')),
            ],
        ),
    ]
