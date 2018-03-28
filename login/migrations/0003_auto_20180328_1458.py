# Generated by Django 2.0.3 on 2018-03-28 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180328_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defuser',
            fields=[
                ('user_name', models.CharField(max_length=60)),
                ('pass_word', models.CharField(max_length=60)),
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='notif',
            name='posted_by_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Defuser'),
        ),
    ]
