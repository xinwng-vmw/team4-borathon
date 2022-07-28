# Generated by Django 4.0.6 on 2022-07-28 20:58

from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_remove_account_account_id_alter_account_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True)),
                ('amount', models.FloatField(default=0.0)),
                ('type', models.BinaryField()),
                ('associated_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]