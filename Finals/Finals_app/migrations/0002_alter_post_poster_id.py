# Generated by Django 3.2 on 2023-02-27 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finals_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster_id',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='Finals_app.users'),
        ),
    ]
