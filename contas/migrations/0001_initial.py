# Generated by Django 4.2.3 on 2023-07-07 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0002_alter_account_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillToPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('value', models.FloatField()),
                ('payment_day', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.category')),
            ],
        ),
        migrations.CreateModel(
            name='PaidBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.billtopay')),
            ],
        ),
    ]
