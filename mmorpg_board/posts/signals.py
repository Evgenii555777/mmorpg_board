from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings
from .models import Comment


def send_notification(to_email, subject, content):
    msg = EmailMultiAlternatives(
        subject=subject,
        body=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email],
    )
    msg.send()


@receiver(post_save, sender=Comment)
def notify_post_author_and_comment_author(sender, instance, created, **kwargs):
    if created:
        post_author_email = instance.post.author.email
        post_author_subject = f"Новый комментарий к вашему посту: {instance.post.title}"
        post_author_content = f"Привет, {instance.post.author.username}!\n\n" \
                              f"К вашему посту \"{instance.post.title}\" был добавлен новый комментарий.\n\n" \
                              f"Комментарий: {instance.text}"
        send_notification(post_author_email, post_author_subject, post_author_content)

    if instance.approved:
        comment_author_email = instance.author.email
        comment_author_subject = f"Ваш комментарий одобрен"
        comment_author_content = f"Привет, {instance.author.username}!\n\n" \
                                 f"Ваш комментарий был одобрен автором поста.\n\n" \
                                 f"Комментарий: {instance.text}"
        send_notification(comment_author_email, comment_author_subject, comment_author_content)
