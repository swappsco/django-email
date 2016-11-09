from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.exceptions import TemplateDoesNotExist
from .exceptions import EmailTemplateNotFound
from .utils import deprecated


def send_email(to=None, message=None, template='base',
               context={}, subject=None):
    """
    Generic Method to Send Emails from template in an easier and modular way
    :param to: Email Address to send the email message
    :param message: Message content that is added to context
    :param template: Path of the email template (Without extension)
    :param context: Dict context variables to send to the template
    :param subject: Email subject
    """
    from_email = settings.DEFAULT_FROM_EMAIL
    if to is None:
        if len(settings.ADMINS) > 0:
            to = settings.ADMINS[0][1]
        else:
            raise AttributeError("Not Admins defined")

    if isinstance(to, (tuple, str)) or isinstance(to, (list, str)):
        pass
    elif unicode:
        if not isinstance(to, unicode):
            raise TypeError(
                "email_to parameter has to be a List, Tuple or a String")
    else:
            raise TypeError(
                "email_to parameter has to be a List, Tuple or a String")

    email_to = to if isinstance(to, tuple) else (to,)

    context.update(get_default_context())

    if message is not None:
        context.update({'message': message})

    try:
        email_template = get_email_template(template)
    except EmailTemplateNotFound:
        email_template = get_email_template('email/base')

    email_subject = subject or "System Notification"

    if email_template.get('txt'):
        template_txt = email_template.get('txt')
        msg = EmailMultiAlternatives(
            email_subject,
            template_txt.render(context), from_email, email_to)
        if email_template.get('html'):
            template_html = email_template.get('html')
            html_content = template_html.render(context)
            msg.attach_alternative(html_content, 'text/html')
        return msg.send()
    else:
        raise AttributeError(".txt template does not exist")

    raise Exception("Could Not Send Email")


def get_default_context():

    default_context = {
        'SITE_NAME': "Django Email",
        'SITE_DOMAIN': "www.example.com"
    }

    if settings.SITE_ID is not None:
        try:
            site = Site.objects.get(id=settings.SITE_ID)
            context = {
                'SITE_NAME': site.name,
                'SITE_DOMAIN': site.domain
            }
        except Site.DoesNotExist:
            context = default_context

    context.update({'TITLE': context.get('SITE_NAME')})

    return context


def get_email_template(template_name):
    has_html, has_txt = True, True
    try:
        html_template = get_template('%s.html' % template_name)
    except TemplateDoesNotExist:
        has_html, html_template = False, None

    try:
        txt_template = get_template('%s.txt' % template_name)
    except TemplateDoesNotExist:
        has_txt, txt_template = False, None

    if has_txt is False:
        raise EmailTemplateNotFound("An Email Template was not found")
    return {
        'txt': txt_template,
        'html': html_template,
    }


class EmailTemplate(object):
    """
    Send emails using templates
    """

    @deprecated
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

    @deprecated
    def set_subject(self, subject):
        self.subject = '%s %s' % (self.subject_prefix, subject)

    @deprecated
    def send_to_user(self, user):
        if user.email:
            self.to = (user.email,)
            self.send()
        else:
            raise ValueError("User does not have a defined email")

    @deprecated
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
