from django.http import HttpResponse
from django_email import djemail


def send_email_view(request):
    """
    Simple example on how to send an email in a view.
    """
    djemail.send_email(
        email_to="email@test.com",
        template_name="email/notification", # .txt and/or .html
        context={'variable': 'Variable Content'},
        subject="My Subject"
    )
    return HttpResponse('Please check your console')
