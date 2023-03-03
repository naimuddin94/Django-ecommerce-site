# Generated by Django 4.1.3 on 2022-11-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_about_section_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('comment', models.TextField(max_length=1000)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]