# Generated by Django 4.2.2 on 2023-07-07 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.CharField(choices=[('student', 'Student'), ('collaborator', 'Collaborator')], default='student', max_length=20, null=True),
        ),
    ]
