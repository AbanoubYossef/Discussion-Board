# Generated by Django 4.2.4 on 2023-09-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_topic_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
