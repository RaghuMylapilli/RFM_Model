# Generated by Django 2.2.6 on 2019-11-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfm_model', '0005_auto_20191124_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutToSleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About_to_Sleep', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='atRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('At_Risk', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cantLoseThem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cant_Lose_Them', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='champions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Champions', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='customersNeedAttention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customers_Needing_Attention', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hibernating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hibernating', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lost', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='loyalCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loyal_Customers', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='potentialLoyalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Potential_Loyalist', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='promising',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Promising', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='recentCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recent_Customers', models.IntegerField(null=True)),
            ],
        ),
    ]
