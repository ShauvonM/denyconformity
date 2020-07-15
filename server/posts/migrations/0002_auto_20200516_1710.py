# Generated by Django 3.0.5 on 2020-05-17 00:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import server.posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='markdown',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='survey_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='survey_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=server.posts.models.PostSummaryField(default='auto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=server.posts.models.PostTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('name', models.TextField()),
                ('time', models.DateTimeField()),
                ('ip', models.GenericIPAddressField()),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('ip', models.GenericIPAddressField()),
                ('why', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='posts.Question')),
            ],
        ),
    ]
