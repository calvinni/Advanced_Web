# Generated by Django 3.2 on 2023-02-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finals_app', '0003_alter_comment_commenter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default='0'),
        ),
    ]
