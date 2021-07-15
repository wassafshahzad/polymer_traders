from traders import celery_app
from django.core.mail import EmailMessage
from django.template.loader import get_template
from tradersapi.util import EmailConstants


@celery_app.task(name="send_welcome_email_on_signup")
def send_welcome_email_on_signup(username, email):
    message = get_template("tradersapi/email.html").render({"username": username})
    mail = EmailMessage(
        subject=EmailConstants.WELCOME_SUBJECT,
        body=message,
        to=[email],
    )
    mail.content_subtype = EmailConstants.HTML_TYPE
    return mail.send()
