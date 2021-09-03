# Generated by Django 3.2.7 on 2021-09-03 13:40

from django.db import migrations, models
import django.db.models.deletion
import icoapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('icoapp', '0006_alter_bid_number_of_tokens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_number_of_token_available', models.IntegerField()),
                ('bidding_window_open', models.DateTimeField()),
                ('bidding_window_closed', models.DateTimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='BidMonitor',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='bid_id',
            new_name='bid',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidding_price',
            field=models.FloatField(validators=[icoapp.models.validate_bid_tokens]),
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='icoapp.user'),
            preserve_default=False,
        ),
    ]
