# Generated by Django 4.1.1 on 2022-09-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(default=1, max_length=13, unique=True),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]