# Generated by Django 3.2.7 on 2021-09-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_state_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='population',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
