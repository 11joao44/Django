# Generated by Django 5.0.4 on 2024-04-09 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contest',
            new_name='content',
        ),
    ]