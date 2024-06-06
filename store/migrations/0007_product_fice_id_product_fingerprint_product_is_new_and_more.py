# Generated by Django 5.0.1 on 2024-06-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fice_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='fingerprint',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='memory',
            field=models.CharField(choices=[('32', '32'), ('64', '64'), ('128', '128'), ('264', '264'), ('512', '512'), ('1024', '1024')], default=1, help_text='GB', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.CharField(choices=[('3', '3'), ('4', '4'), ('6', '6'), ('8', '8'), ('12', '12')], default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='color',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
