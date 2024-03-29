# Generated by Django 2.1.5 on 2019-06-06 19:13

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
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='Insira sua biografia aqui.', max_length=500)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datahora', models.DateTimeField(auto_now_add=True)),
                ('conteudo', models.CharField(help_text='Escreva seu comentario', max_length=1000)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog_app.Autor')),
            ],
            options={
                'ordering': ['datahora'],
            },
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Escreva o título da postagem', max_length=100)),
                ('datahora', models.DateTimeField(auto_now_add=True)),
                ('conteudo', models.CharField(help_text='Escreva sua postagem', max_length=1000)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog_app.Autor')),
            ],
            options={
                'ordering': ['-datahora'],
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Postagem'),
        ),
    ]
