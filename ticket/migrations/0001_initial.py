# Generated by Django 4.2.4 on 2023-08-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road', models.CharField(max_length=200)),
                ('space', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
