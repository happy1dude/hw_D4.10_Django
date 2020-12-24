# Generated by Django 3.1.4 on 2020-12-23 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20201219_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_house', models.TextField()),
                ('books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='p_library.book')),
            ],
        ),
    ]