# Generated by Django 2.2.1 on 2019-05-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_delete_man'),
    ]

    operations = [
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(db_index=True, max_length=150)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
