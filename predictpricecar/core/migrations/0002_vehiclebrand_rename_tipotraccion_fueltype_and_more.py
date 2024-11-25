# Generated by Django 4.2.16 on 2024-11-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='TipoTraccion',
            new_name='FuelType',
        ),
        migrations.RenameModel(
            old_name='EstadoGeneralVehiculo',
            new_name='TractionType',
        ),
        migrations.RenameModel(
            old_name='TipoCombustible',
            new_name='TransmissionType',
        ),
        migrations.RenameModel(
            old_name='TipoTransmision',
            new_name='VehicleCondition',
        ),
        migrations.DeleteModel(
            name='MarcaVehiculo',
        ),
        migrations.RemoveField(
            model_name='tipousuario',
            name='modulos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_usuario',
        ),
        migrations.RenameField(
            model_name='fueltype',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='fueltype',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tractiontype',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tractiontype',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='transmissiontype',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='transmissiontype',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vehiclecondition',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='vehiclecondition',
            old_name='nombre',
            new_name='name',
        ),
        migrations.DeleteModel(
            name='Modulo',
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
