from django.core.mail import send_mail
from EmailNotificationService.EmailNotificationService.settings import EMAIL_HOST_USER

def sendEmailNotification():
    subject = 'Email Test Subject'
    message = 'Test Email Body Message'
    recepient = str("someeami@gmail.com")
    send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently=True)


def send_email():
    email = EmailMessage(
        'Title',
        (ConsultSerializer.name, ConsultSerializer.email, ConsultSerializer.phone),
        'my-email',
        ['my-receive-email']
    )
    email.attach_file(ConsultSerializer.file)
    email.send()
