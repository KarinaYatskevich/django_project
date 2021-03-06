# Generated by Django 3.2 on 2021-05-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_musicband_alb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicband',
            old_name='alb',
            new_name='album',
        ),
        migrations.RemoveField(
            model_name='musicband',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='album',
            name='track',
        ),
        migrations.AddField(
            model_name='album',
            name='track',
            field=models.ManyToManyField(to='home.Track'),
        ),
    ]
