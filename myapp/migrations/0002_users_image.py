# Generated by Django 4.0.3 on 2022-04-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]