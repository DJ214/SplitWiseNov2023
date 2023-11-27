import asyncio
from django.core.mail import send_mail


async def send_expense_notification(email, transactions):
    subject = 'Expense Notification'
    message = f'You have been added to an expense. Total amount owed: {transactions}.'
    from_email = 'your_email@example.com'
    recipient_list = [email]
    await asyncio.sleep(1)  # Simulate an asynchronous task
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
