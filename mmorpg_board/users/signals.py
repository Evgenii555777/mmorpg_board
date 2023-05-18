from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
import secrets

@receiver(post_save, sender=User)
def send_registration_confirmation(sender, instance, created, **kwargs):
    if created:
        confirmation_code = secrets.token_hex(8)
        if hasattr(instance, 'profile'):
            instance.profile.code = int(confirmation_code, 16)
            instance.profile.is_confirmed = True
            instance.profile.save()

        subject = 'Подтверждение регистрации'
        message = f'Спасибо за регистрацию! Ваш код подтверждения: {confirmation_code}'
        from_email = 'SkillFactoryTest@yandex.ru'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)

