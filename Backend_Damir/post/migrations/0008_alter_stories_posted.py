# Generated by Django 4.0.3 on 2022-05-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_stories_readers_alter_stories_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='posted',
            field=models.DateTimeField(),
        ),
    ]
