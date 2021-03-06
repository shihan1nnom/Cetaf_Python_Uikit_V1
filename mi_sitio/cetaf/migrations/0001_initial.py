# Generated by Django 3.1.3 on 2021-06-27 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('num_serie', models.CharField(max_length=50)),
                ('fecha_compra', models.DateField()),
                ('cobertura_seguro', models.CharField(max_length=200)),
                ('valor_compra', models.IntegerField(default=0)),
                ('garantia', models.CharField(max_length=200)),
                ('fecha_puesto_servicio', models.DateField()),
                ('descripcion', models.TextField()),
                ('vida_util', models.CharField(max_length=200)),
                ('valor_residual', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_responsable', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('descripcion', models.TextField()),
                ('ambiente_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cetaf.ambiente')),
                ('nombre_activo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cetaf.activo')),
                ('sede_asignada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cetaf.sede')),
            ],
        ),
        migrations.AddField(
            model_name='activo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cetaf.categoria'),
        ),
    ]
