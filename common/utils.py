import os

from django.conf import settings
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_order_invoice_email(order):
    to_emails = [
        # 'cimi-omeri@hotmail.com',
        'klementomeri97@gmail.com',
        ]
    if order.email:
        to_emails.append(order.email)

    context = {
        'order_identifier': f'ITG-{order.id}',
        'invoice_url': f'{settings.FRONTEND_INVOICE_URL}/{order.id}'
        }
    html = render_to_string(
            template_name='email/order_saved.html',
            context=context
            )

    message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=to_emails,
            subject=f'[ITALGOLD] Porosia {context["order_identifier"]}',
            html_content=html
            )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))
