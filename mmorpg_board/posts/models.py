from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    CATEGORIES = [
        ("TNK", "Танки"),
        ("HIL", "Хилы"),
        ("DD", "ДД"),
        ("TRD", "Торговцы"),
        ("GDM", "Гилдмастеры"),
        ("QGV", "Квестгиверы"),
        ("BSM", "Кузнецы"),
        ("LTH", "Кожевники"),
        ("ALC", "Зельевары"),
        ("ENC", "Мастера заклинаний"),
    ]

    title = models.CharField("Заголовок", max_length=200)
    image = models.ImageField(upload_to='post_images/')
    video = models.FileField(upload_to='post_videos/', null=True, blank=True)
    text = models.TextField("Текст")
    category = models.CharField("Категория", max_length=3, choices=CATEGORIES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField("Комментарий")

    def __str__(self):
        return f"{self.author.username}'s Comment"
