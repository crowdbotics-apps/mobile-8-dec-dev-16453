# Generated by Django 2.2.17 on 2020-12-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abcd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abcd', models.BigIntegerField()),
            ],
        ),
    ]
