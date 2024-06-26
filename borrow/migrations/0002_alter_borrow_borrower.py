# Generated by Django 5.0.4 on 2024-06-21 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0001_initial'),
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='borrowers', to='user_account.useraccount'),
        ),
    ]
