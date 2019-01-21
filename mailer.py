from django.core.mail import send_mail


def mailer():
    send_mail(
        'merchant receipt',
        'Here is the message.',
        'zoaby.am@gmail.com',
        ['z3by.ahmad@gmail.com'],
        fail_silently=False,
    )
