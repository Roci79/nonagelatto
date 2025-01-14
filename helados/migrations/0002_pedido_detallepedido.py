# Generated by Django 5.0.3 on 2024-03-27 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('sabor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helados.sabor')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helados.pedido')),
            ],
        ),
    ]
