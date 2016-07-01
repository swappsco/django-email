from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib.sites.models import Site


class EmailTemplate(object):
    """
    Send emails using templates
    """

    def __init__(self, template_name, context=None):
        if template_name:
            self.template = template_name
        self.from_email = settings.DJANGO_EMAIL_FROM or None
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
            self.subject, plaintext.render(self.context), self.from_email, self.to)
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
