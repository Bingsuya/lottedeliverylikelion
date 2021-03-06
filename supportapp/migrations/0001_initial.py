# Generated by Django 3.1.2 on 2020-10-25 07:47

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
            name='Qna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_title', models.CharField(max_length=200)),
                ('q_content', models.TextField()),
                ('q_type', models.CharField(max_length=200)),
                ('q_boxcode', models.CharField(max_length=30)),
                ('q_time', models.DateTimeField(auto_now=True)),
                ('public', models.BooleanField(null=True)),
                ('pic', models.ImageField(null=True, upload_to='%Y/%m/%d')),
                ('today', models.IntegerField(default='0')),
                ('answers', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=200)),
                ('a_contents', models.TextField()),
                ('a_time', models.DateTimeField(auto_now=True)),
                ('a_qna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supportapp.qna')),
            ],
        ),
    ]
