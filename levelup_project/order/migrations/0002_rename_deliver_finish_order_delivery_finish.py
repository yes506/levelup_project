# Generated by Django 4.0 on 2022-01-04 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='deliver_finish',
            new_name='delivery_finish',
        ),
    ]
