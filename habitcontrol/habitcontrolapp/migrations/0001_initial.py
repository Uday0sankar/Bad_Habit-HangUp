# Generated by Django 4.1.7 on 2023-03-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hab_img', models.ImageField(upload_to='pics')),
                ('hab_name', models.CharField(max_length=150)),
            ],
        ),
    ]
