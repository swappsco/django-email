from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.exceptions import TemplateDoesNotExist
from .exceptions import EmailTemplateNotFound


def send_email(email_to, template_name, context={}, subject=None):
    """
    Generic Method to Send Emails from template in an easier and modular way
    :param to: Email Address to send the email message
    :param template_name: Path of the email template (Without extension)
    :param context: Dict context variables to send to the template
    :param subject: Email subject
    """
    from_email = settings.DEFAULT_FROM_EMAIL

    if not isinstance(email_to, (tuple, str)):
        raise TypeError("email_to parameter has to be a Tuple or a String")

    to = email_to if isinstance(email_to, tuple) else (email_to,)

    try:
        email_template = get_email_template(template_name)
    except EmailTemplateNotFound:
        print("EmailTemplate Not found")
        return False

    email_subject = subject or "System Notification"

    if email_template.get('txt'):
        template_txt = email_template.get('txt')
        msg = EmailMultiAlternatives(
            email_subject,
            template_txt.render(context), from_email, to)
        if email_template.get('html'):
            template_html = email_template.get('html')
            html_content = template_html.render(context)
            msg.attach_alternative(html_content, 'text/html')
        msg.send()


def get_email_template(template_name):
    has_html, has_txt = True, True
    print(template_name)
    try:
        html_template = get_template('%s.html' % template_name)
    except TemplateDoesNotExist:
        has_html, html_template = False, None

    try:
        txt_template = get_template('%s.txt' % template_name)
    except TemplateDoesNotExist:
        has_txt, txt_template = False, None

    if has_html is False and has_txt is False:
        raise EmailTemplateNotFound("An Email Template was not found")
    return {
        'txt': txt_template,
        'html': html_template,
    }


class EmailTemplate(object):
    """
    Send emails using templates
    """

    def __init__(self, template_name, context=None):
        if template_name:
            self.template = template_name
        self.from_email = settings.DEFAULT_FROM_EMAIL or None
        self.subject = 'django-email Notification'
        self.to = (settings.DJANGO_EMAIL_ADMIN,)
        self.title = self.subject
        if context is None:
            self.context = {'title': self.title}
        else:
            self.context = context
        self.site = Site.objects.get(pk=settings.SITE_ID)

        try:
            self.subject_prefix = settings.DJANGO_EMAIL_SUBJECT_PREFIX
        except AttributeError:
            self.subject_prefix = ''

    def set_subject(self, subject):
        self.subject = '%s %s' % (self.subject_prefix, subject)

    def send_to_user(self, user):
        if user.email:
            self.to = (user.email,)
            self.send()
        else:
            raise ValueError("User does not have a defined email")

    def send(self):
        if not self.to:
            raise ValueError("User does not have a defined email")

        self.context['base_url'] = self.site.domain
        plaintext = get_template('email/%s.txt' % (self.template))
        htmly = get_template('email/%s.html' % (self.template))

        html_content = htmly.render(self.context)
        msg = EmailMultiAlternatives(
            self.subject,
            plaintext.render(self.context), self.from_email, self.to)
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
