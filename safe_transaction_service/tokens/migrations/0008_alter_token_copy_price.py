# Generated by Django 4.0.2 on 2022-03-07 09:35

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):
    dependencies = [
        ("tokens", "0007_alter_token_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="copy_price",
            field=gnosis.eth.django.models.EthereumAddressV2Field(
                blank=True,
                help_text="If provided, copy the price from the token",
                null=True,
            ),
        ),
    ]
