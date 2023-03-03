# Generated by Django 4.1.3 on 2022-11-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('heading', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]
