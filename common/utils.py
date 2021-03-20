from django.conf import settings
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sentry_sdk import capture_exception


def get_order_email(order) -> Mail:
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

    return Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=to_emails,
            subject=f'[ITALGOLD] Porosia {context["order_identifier"]}',
            html_content=render_to_string(
                    template_name='email/order_saved.html',
                    context=context
                    )
            )


def send_order_invoice_email(order):
    try:
        SendGridAPIClient().send(message=get_order_email(order))
    except Exception as e:
        capture_exception(e)
        print(str(e))


def dictfetchall(cursor) -> list:
    """
    Returns all rows from a cursor as a list with dicts.
    :param cursor: Cursor object
    :return: List of dicts with results
    """
    return [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
