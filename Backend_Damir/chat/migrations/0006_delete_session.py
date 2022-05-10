from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_session'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Session',
        ),
    ]