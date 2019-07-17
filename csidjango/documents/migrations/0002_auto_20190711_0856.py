# Generated by Django 2.2.1 on 2019-07-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='manual',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='procedure',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='date_actived',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='date_deactived',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manual',
            name='date_actived',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manual',
            name='date_deactived',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='date_actived',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='date_deactived',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]