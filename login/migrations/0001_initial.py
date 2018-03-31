# Generated by Django 2.0.3 on 2018-03-31 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comp_match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Compliant',
            fields=[
                ('add_date', models.DateField()),
                ('status', models.CharField(max_length=120)),
                ('explain', models.CharField(max_length=800)),
                ('about', models.CharField(max_length=60)),
                ('sub', models.CharField(max_length=200)),
                ('comp_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Defuser',
            fields=[
                ('user_name', models.CharField(max_length=60)),
                ('pass_word', models.CharField(max_length=60)),
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fee_pay',
            fields=[
                ('paid_date', models.DateTimeField()),
                ('fee_paid', models.IntegerField()),
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('data', models.CharField(max_length=1500)),
                ('head', models.CharField(max_length=500)),
                ('posted_by_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Defuser')),
            ],
        ),
        migrations.CreateModel(
            name='Paying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Fee_pay')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('pass_word', models.CharField(max_length=60)),
                ('father_name', models.CharField(max_length=120)),
                ('mother_name', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('branch', models.CharField(max_length=60)),
                ('admission_number', models.CharField(max_length=20)),
                ('ten_res', models.FloatField()),
                ('puc_res', models.FloatField()),
                ('reg_no', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=120)),
                ('fee', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('Temp_address', models.CharField(max_length=800)),
                ('per_address', models.CharField(max_length=800)),
                ('studying_year', models.CharField(max_length=9)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='paying',
            name='std_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
        migrations.AddField(
            model_name='comp_match',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Compliant'),
        ),
        migrations.AddField(
            model_name='comp_match',
            name='regno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
