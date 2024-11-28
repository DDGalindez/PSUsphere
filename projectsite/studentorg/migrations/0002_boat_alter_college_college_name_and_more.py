# Generated by Django 5.1.2 on 2024-11-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat_name', models.CharField(max_length=150)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(max_length=150, verbose_name='College'),
        ),
        migrations.AlterField(
            model_name='program',
            name='prog_name',
            field=models.CharField(max_length=150, verbose_name='Program Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=25, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=25, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middlename',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Middle Name'),
        ),
    ]
