# Generated by Django 3.2.9 on 2022-01-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
    ]
