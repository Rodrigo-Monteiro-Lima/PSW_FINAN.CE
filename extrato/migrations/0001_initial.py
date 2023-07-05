# Generated by Django 4.2.3 on 2023-07-05 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0002_alter_account_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('value_type', models.CharField(choices=[('I', 'Income'), ('O', 'Outcome')], max_length=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.category')),
            ],
        ),
    ]