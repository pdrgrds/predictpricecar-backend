# Generated by Django 4.2.16 on 2024-11-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_module_usertype_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('admin', 'Admin')], default='normal', max_length=10),
        ),
    ]
