# Generated by Django 3.0.1 on 2020-01-01 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200101_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
