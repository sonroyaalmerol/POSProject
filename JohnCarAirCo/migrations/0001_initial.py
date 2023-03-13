# Generated by Django 4.1.7 on 2023-03-13 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=255)),
                ('customerContact', models.CharField(max_length=12)),
                ('customerEmail', models.CharField(max_length=255)),
                ('customerAddress', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('unitName', models.CharField(choices=[('Split Type', 'Split Type'), ('Window Air Conditioner', 'Window Air Conditioner'), ('N/A', 'N/A')], default='N/A', max_length=255, primary_key=True, serialize=False)),
                ('unitPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('unitQuantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('serviceChoice', models.CharField(choices=[('Cars', 'Cars'), ('House', 'House'), ('Office', 'Office'), ('N/A', 'N/A')], default='N/A', max_length=50, primary_key=True, serialize=False)),
                ('estimatedCost', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppName', models.CharField(max_length=255)),
                ('suppPhone', models.CharField(max_length=12)),
                ('suppEmail', models.CharField(max_length=255)),
                ('suppAddress', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicianDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techName', models.CharField(max_length=255)),
                ('techPhone', models.CharField(max_length=12)),
                ('techEmail', models.CharField(max_length=255)),
                ('techSched', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOrdered', models.DateField(auto_now_add=True)),
                ('serviceDate', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Finished', 'Finished'), ('Cancelled', 'Cancelled')], default='Active', max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.customerdetails')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.servicetype')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.techniciandetails')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOrdered', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Finished', 'Finished'), ('Cancelled', 'Cancelled')], default='Active', max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.customerdetails')),
                ('products', models.ManyToManyField(through='JohnCarAirCo.OrderItem', to='JohnCarAirCo.productunit')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('deliveryDate', models.DateField()),
                ('itemDesc', models.CharField(max_length=255)),
                ('itemQuantity', models.PositiveIntegerField()),
                ('itemCost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('customerName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.customerdetails')),
                ('supplierName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.supplierdetails')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.salesorder'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JohnCarAirCo.productunit'),
        ),
    ]
