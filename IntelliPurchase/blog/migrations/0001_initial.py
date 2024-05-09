# Generated by Django 5.0.4 on 2024-05-09 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('category_id', models.IntegerField()),
                ('TGDD_product_link', models.URLField()),
                ('FPT_product_link', models.URLField()),
                ('image', models.URLField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductSpec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=100)),
                ('screen', models.CharField(max_length=100)),
                ('rear_camera', models.CharField(max_length=100)),
                ('front_camera', models.CharField(max_length=100)),
                ('OS_CPU', models.CharField(max_length=100)),
                ('memory_storage', models.CharField(max_length=100)),
                ('ket_noi', models.CharField(max_length=100)),
                ('pin_sac', models.CharField(max_length=100)),
                ('tien_ich', models.CharField(max_length=100)),
                ('thongtin_chung', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product')),
            ],
            options={
                'db_table': 'technical_details',
            },
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.TextField()),
                ('s_pin', models.TextField(null=True)),
                ('s_general', models.TextField(null=True)),
                ('s_service', models.TextField(null=True)),
                ('s_others', models.TextField(null=True)),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='blog.product')),
            ],
            options={
                'db_table': 'average_sa',
            },
        ),
        migrations.AddConstraint(
            model_name='sentiment',
            constraint=models.UniqueConstraint(fields=('product_id', 'company_id'), name='unique_sentiment'),
        ),
    ]
