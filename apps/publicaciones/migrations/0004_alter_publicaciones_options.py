# Generated by Django 4.2.7 on 2023-12-25 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_alter_categoria_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicaciones',
            options={'ordering': ('-fecha',)},
        ),
    ]