# Generated by Django 3.1.4 on 2020-12-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'book', 'verbose_name_plural': 'books'},
        ),
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
