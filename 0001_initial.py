# Generated by Django 4.1.5 on 2023-01-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=50)),
                ('Product_Company_Name', models.CharField(max_length=50)),
                ('Product_Image', models.ImageField(upload_to=None, width_field=100)),
                ('Product_Price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Entered_by', models.CharField(max_length=50)),
            ],
        ),
    ]
