# Generated by Django 4.0.5 on 2022-11-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Gasto',
                'verbose_name_plural': 'Gastos',
                'ordering': ['fecha'],
            },
        ),
    ]