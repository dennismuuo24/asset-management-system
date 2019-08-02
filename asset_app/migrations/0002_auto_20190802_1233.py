# Generated by Django 2.2.4 on 2019-08-02 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=100)),
                ('asset_serial_No', models.CharField(max_length=100)),
                ('asset_location', models.CharField(max_length=100)),
                ('asset_manufacturer', models.CharField(max_length=100)),
                ('date_purchased', models.DateTimeField()),
                ('asset_issued', models.BooleanField()),
                ('date_issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('asset_image', models.ImageField(default='default.jpeg', upload_to='images/')),
                ('asset_assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='neighborhood',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Neighborhood',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
