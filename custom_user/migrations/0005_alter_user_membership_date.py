# Generated by Django 5.0.2 on 2024-03-02 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0004_alter_user_membership_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='membership_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
