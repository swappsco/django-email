from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.contrib.sites.models import Site


class EmailTemplate(object):
    """
    Send emails using templates
    """

    def __init__(self, template_name, context=None):
        if template_name:
            self.template = template_name
        self.from_email = settings.DJANGO_EMAIL_FROM
        self.subject = 'django-email Notification'
        self.to = (settings.DJANGO_EMAIL_ADMIN,)
        self.title = self.subject
        if not context:
            self.context = {'title': self.title}
        self.site = Site.objects.get(pk=settings.SITE_ID)

        if settings.DJANGO_EMAIL_SUBJECT_PREFIX:
            self.subject_prefix = settings.DJANGO_EMAIL_SUBJECT_PREFIX
        else:
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
        # plaintext = get_template('email/'+self.template+'.txt')
        htmly = get_template('email/%s.html' % self.template)

        d = Context(self.context)

        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(
            self.subject, html_content, self.from_email, self.to)
        msg.content_subtype = "html"
        msg.send()
