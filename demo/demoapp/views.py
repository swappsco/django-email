from django.http import HttpResponse
from django_email.email import EmailTemplate


def send_email_view(request):
    """
    Simple example on how to send an email in a view.
    """
    context = {'body': 'This is some body'}
    template = 'base'
    email_template = EmailTemplate(template, context)
    email_template.set_subject('My demo email')
    request.user.email = 'test@test.com'
    email_template.send_to_user(request.user)
    return HttpResponse('Please check your console')
