# Generated by Django 2.0.1 on 2019-12-30 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]