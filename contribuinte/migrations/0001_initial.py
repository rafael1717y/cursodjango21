# Generated by Django 3.1.7 on 2021-03-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribuinte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=255)),
                ('contato', models.TextField(blank=True)),
            ],
        ),
    ]
