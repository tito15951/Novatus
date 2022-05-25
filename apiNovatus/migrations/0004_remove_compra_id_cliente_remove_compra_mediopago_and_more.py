# Generated by Django 4.0.3 on 2022-05-17 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiNovatus', '0003_usuario_marca_moto_alter_usuario_direccion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='id_cliente',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='medioPago',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='id_compra',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='vendedor',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='marca_moto',
        ),
        migrations.AddField(
            model_name='cita',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cita',
            name='placa_moto',
            field=models.TextField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='comentario',
            name='id_cita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apiNovatus.cita'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]