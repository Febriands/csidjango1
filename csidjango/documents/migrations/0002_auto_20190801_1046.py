# Generated by Django 2.2.1 on 2019-08-01 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('standar_doc', models.FileField(blank=True, null=True, upload_to='standar/')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='form',
            old_name='form',
            new_name='form_doc',
        ),
        migrations.RenameField(
            model_name='manual',
            old_name='manual',
            new_name='manual_doc',
        ),
        migrations.RenameField(
            model_name='procedure',
            old_name='procedure',
            new_name='procedure_doc',
        ),
        migrations.AddField(
            model_name='form',
            name='manual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_manual', to='documents.Manual'),
        ),
        migrations.AddField(
            model_name='form',
            name='procedure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_procedure', to='documents.Procedure'),
        ),
        migrations.AddField(
            model_name='form',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='manual',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='procedure',
            name='manual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manual_procedure', to='documents.Manual'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='manual',
            name='standar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manual_standar', to='documents.Standar'),
        ),
    ]
