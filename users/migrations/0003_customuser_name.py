# Generated by Django 4.2.4 on 2023-09-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=110, null=True),
        ),
    ]
