# Generated by Django 5.0.4 on 2024-04-09 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_rename_user_comments_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='name',
            new_name='user',
        ),
    ]
