# Generated by Django 2.2.9 on 2020-01-17 14:49

from django.db import migrations, models
import shorturl.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=shorturl.models.get_key, max_length=6, unique=True)),
                ('origin', models.URLField(verbose_name='원본 url 주소')),
            ],
            options={
                'verbose_name_plural': '라우트',
            },
        ),
    ]
