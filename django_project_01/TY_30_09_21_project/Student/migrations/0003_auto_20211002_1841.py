# Generated by Django 3.2.7 on 2021-10-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20211002_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_information',
            name='CGPA',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_information',
            name='RollNo',
            field=models.IntegerField(),
        ),
    ]