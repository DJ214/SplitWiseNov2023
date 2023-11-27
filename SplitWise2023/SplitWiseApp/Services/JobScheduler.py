from celery import shared_task
from django.core.mail import send_mail

from .. import models
from ..models import User
from ..models import Transaction
import asyncio

@shared_task
def send_weekly_email():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_send_weekly_email())

async def _send_weekly_email():
    users = User.objects.all()

    for user in users:
        total_owed = Transaction.objects.filter(payee=user).aggregate(total_owed=models.Sum('amount'))['total_owed'] or 0

        subject = 'Weekly Owing Summary'
        message = f'Hello {user.name},\n\nYou owe a total of {total_owed} this week.\n\nBest regards,\nYour App Team'

        from_email = 'your_email@example.com'  # Replace with your email
        recipient_list = [user.email]

        await send_mail(subject, message, from_email, recipient_list, fail_silently=False)