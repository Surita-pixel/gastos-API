# Generated by Django 4.1.3 on 2022-12-14 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_id_usuario_userio_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='userio_id',
            new_name='usuario_id',
        ),
    ]