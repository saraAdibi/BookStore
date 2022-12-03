# Generated by Django 3.2.9 on 2022-01-21 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Factors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ پرداخت')),
                ('state', models.SmallIntegerField(choices=[(1, 'پرداخت نشده'), (2, 'در انتظار پرداخت'), (3, 'پرداخت شده')], default=1, verbose_name='وضعیت پرداخت')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ایجاد')),
                ('total_price', models.PositiveIntegerField(verbose_name='مبلغ نهایی')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری')),
            ],
        ),
        migrations.CreateModel(
            name='FactorProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='تعداد')),
                ('total_price', models.PositiveIntegerField(verbose_name='مبلغ نهایی')),
                ('id_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factor.factors', verbose_name='فاکتور')),
                ('id_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='نام محصول')),
            ],
        ),
    ]