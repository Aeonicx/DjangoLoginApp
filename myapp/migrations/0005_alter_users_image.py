# Generated by Django 4.0.3 on 2022-04-02 20:38

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_users_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(default='uploads/default.png', upload_to=myapp.models.filepath),
        ),
    ]
