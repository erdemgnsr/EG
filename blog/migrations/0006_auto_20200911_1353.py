# Generated by Django 3.0.5 on 2020-09-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200911_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_1',
            field=models.FileField(blank=True, default='buyap.jpeg', null=True, upload_to='', verbose_name='Makaleye içerik ekleyin'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_2',
            field=models.FileField(blank=True, default='buyap.jpeg', null=True, upload_to='', verbose_name='Makaleye içerik ekleyin'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_3',
            field=models.FileField(blank=True, default='buyap.jpeg', null=True, upload_to='', verbose_name='Makaleye içerik ekleyin'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_4',
            field=models.FileField(blank=True, default='buyap.jpeg', null=True, upload_to='', verbose_name='Makaleye içerik ekleyin'),
        ),
    ]
