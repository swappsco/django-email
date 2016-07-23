#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-email
------------

Tests for `django-email` models module.
"""

from django.test import TestCase
from django_email import djemail
from django.contrib.sites.models import Site

class EmailTest(TestCase):
    def test_send_email(self):
		mail = djemail.send_email(
		    email_to="email@test.com",
		    template_name="email/base", # .txt and/or .html
		    context={'variable': 'Variable Content'},
		    subject="My Subject"
		)
		self.assertEquals(mail.subject, 'My Subject')
		self.assertEquals(mail.to, ["email@test.com"])
