# Generated by Django 5.1.2 on 2024-10-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('loanno', models.IntegerField(primary_key='Loanno', serialize=False)),
                ('loanamnt', models.IntegerField()),
                ('dob', models.DateField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
