# Generated by Django 4.0.6 on 2022-07-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_bio_user_birthday_user_block_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, error_messages={'error': 'Bunday email mavjud.'}, max_length=254, unique=True, verbose_name='email'),
            preserve_default=False,
        ),
    ]