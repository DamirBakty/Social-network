# Generated by Django 4.0.3 on 2022-04-19 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageimage',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messageimage',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='MessageImage',
        ),
    ]
