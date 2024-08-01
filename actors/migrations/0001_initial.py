# Generated by Django 5.0.5 on 2024-05-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil')], default='USA', max_length=100)),
            ],
        ),
    ]
