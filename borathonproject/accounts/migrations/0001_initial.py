# Generated by Django 4.0.6 on 2022-07-29 17:50

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False, unique=True)),
                ('account_number', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True)),
                ('balance', models.FloatField(default=0.0)),
                ('account_status', models.BinaryField()),
            ],
        ),
    ]
