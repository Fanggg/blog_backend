# Generated by Django 2.1.4 on 2019-02-26 06:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInformation',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('git', models.CharField(max_length=128, null=True)),
                ('url', models.CharField(max_length=128, null=True)),
                ('weChat', models.CharField(max_length=128, null=True)),
                ('location', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', ckeditor.fields.RichTextField()),
                ('synopsis', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', '草稿'), ('public', '公开')], default='draft', max_length=8)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=128000, null=True)),
                ('location', models.CharField(max_length=128000, null=True)),
                ('entrance', models.CharField(max_length=128000, null=True)),
                ('country', models.CharField(max_length=128000, null=True)),
                ('area', models.CharField(max_length=128000, null=True)),
                ('region', models.CharField(max_length=128000, null=True)),
                ('city', models.CharField(max_length=128000, null=True)),
                ('isp', models.CharField(max_length=128000, null=True)),
                ('access_tools', models.CharField(max_length=128000, null=True)),
                ('JSON', models.TextField(null=True)),
                ('action', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pond_IP',
            fields=[
                ('ip', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='上次来访时间')),
                ('visit_number', models.IntegerField(default=1, editable=False, null=True, verbose_name='来访次数')),
            ],
        ),
        migrations.CreateModel(
            name='ReplySummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('ip', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blog.Pond_IP')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='上次拦截时间')),
                ('intercept_number', models.IntegerField(default=0, editable=False, null=True, verbose_name='拦截次数')),
            ],
        ),
        migrations.AddField(
            model_name='replysummary',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operatorReply', to='blog.User'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operator', to='blog.User'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='reply',
            field=models.ManyToManyField(blank=True, to='blog.ReplySummary'),
        ),
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='blog.User'),
        ),
    ]
