# Generated by Django 2.0.1 on 2018-01-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180128_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='campaign',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]