# Generated by Django 3.2.16 on 2023-01-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230104_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='intro',
            new_name='excerpt',
        ),
    ]