# Generated by Django 4.2.7 on 2023-11-04 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='d_o_b',
            new_name='date_of_birth',
        ),
    ]
