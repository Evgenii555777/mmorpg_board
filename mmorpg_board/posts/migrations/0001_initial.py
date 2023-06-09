# Generated by Django 4.2.1 on 2023-05-16 08:46

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='post_images/', verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Текст')),
                ('category', models.CharField(choices=[('TNK', 'Танки'), ('HIL', 'Хилы'), ('DD', 'ДД'), ('TRD', 'Торговцы'), ('GDM', 'Гилдмастеры'), ('QGV', 'Квестгиверы'), ('BSM', 'Кузнецы'), ('LTH', 'Кожевники'), ('ALC', 'Зельевары'), ('ENC', 'Мастера заклинаний')], max_length=3, verbose_name='Категория')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post')),
            ],
        ),
    ]
