# Generated by Django 3.2 on 2023-02-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finals_app', '0004_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to='Finals_app.Users'),
        ),
    ]
