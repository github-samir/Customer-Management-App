# Generated by Django 3.1 on 2020-08-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200816_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Sent', 'Sent'), ('Delivered', 'Delivered')], max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
