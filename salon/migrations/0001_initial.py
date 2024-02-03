# Generated by Django 4.2.9 on 2024-01-12 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('service', models.ManyToManyField(related_name='customersbook', to='salon.service')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True)),
                ('date_appoint', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.package')),
                ('services', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.service')),
            ],
        ),
    ]
