# Generated by Django 3.1.6 on 2021-02-17 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller_accounts', '0002_auto_20210207_2127'),
        ('product', '0008_auto_20210207_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller_accounts.seller'),
        ),
    ]
