# Generated by Django 3.0.7 on 2022-12-13 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sonha', models.CharField(blank=True, max_length=250, null=True)),
                ('duong', models.CharField(blank=True, max_length=250, null=True)),
                ('phuong', models.CharField(blank=True, max_length=250, null=True)),
                ('quan', models.CharField(blank=True, max_length=250, null=True)),
                ('createdate', models.DateTimeField(blank=True, null=True)),
                ('editdate', models.DateTimeField(blank=True, null=True)),
                ('isenable', models.IntegerField(blank=True, null=True)),
                ('creator_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'House',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('keyname', models.CharField(blank=True, max_length=250, null=True)),
                ('createdate', models.DateTimeField(blank=True, null=True)),
                ('editdate', models.DateTimeField(blank=True, null=True)),
                ('isenable', models.IntegerField(blank=True, null=True)),
                ('creator_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'AccountType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tenthanh', models.CharField(blank=True, max_length=250, null=True)),
                ('giatruong', models.CharField(blank=True, max_length=250, null=True)),
                ('sinhnhat', models.CharField(blank=True, max_length=250, null=True)),
                ('phaitinh', models.CharField(blank=True, max_length=250, null=True)),
                ('bitich', models.CharField(blank=True, max_length=250, null=True)),
                ('giaoly', models.CharField(blank=True, max_length=250, null=True)),
                ('honnhan', models.CharField(blank=True, max_length=250, null=True)),
                ('hocvan', models.CharField(blank=True, max_length=250, null=True)),
                ('nghenghiep', models.CharField(blank=True, max_length=250, null=True)),
                ('thunhap', models.CharField(blank=True, max_length=250, null=True)),
                ('dienthoai', models.CharField(blank=True, max_length=250, null=True)),
                ('createdate', models.DateTimeField(blank=True, null=True)),
                ('editdate', models.DateTimeField(blank=True, null=True)),
                ('accounttypeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.AccountType')),
                ('creator_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_user', to=settings.AUTH_USER_MODEL)),
                ('houseid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.House')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Account',
                'managed': True,
            },
        ),
    ]