# Generated by Django 4.0.4 on 2022-05-27 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=30)),
                ('contrasenia', models.TextField(max_length=20)),
                ('direccion', models.TextField(max_length=20, null=True)),
                ('telefono', models.TextField(max_length=10, null=True)),
                ('rol', models.TextField(default='cliente', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=20)),
                ('direccion', models.TextField(max_length=20)),
                ('valoracion', models.IntegerField(default=0)),
                ('tel', models.TextField(max_length=10)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('num_tarjeta', models.TextField(max_length=16)),
                ('cod_seguridad', models.TextField(max_length=3)),
                ('fecha_venc', models.TextField(max_length=5)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('puntuacion', models.IntegerField(default=0)),
                ('id_tienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.tienda')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hora', models.DateTimeField()),
                ('duracion', models.IntegerField(default=0)),
                ('descripcion', models.TextField(max_length=200)),
                ('placa_moto', models.TextField(default='', max_length=6)),
                ('id_tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.tienda')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mensaje', models.TextField(max_length=150)),
                ('hora', models.DateTimeField(auto_now=True, null=True)),
                ('cita', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.cita')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='apiNovatus.usuario')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origen', to='apiNovatus.usuario')),
            ],
        ),
    ]
