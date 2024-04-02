# Generated by Django 5.0.3 on 2024-03-19 04:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('count_like', models.IntegerField(blank=True, default=0, verbose_name='좋아요 수')),
                ('count_comment', models.IntegerField(blank=True, default=0, verbose_name='답변 수')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
