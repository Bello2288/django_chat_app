# Generated by Django 4.1.2 on 2022-10-18 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='author',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.RemoveField(
            model_name='room',
            name='title',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='chat',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.room'),
        ),
    ]