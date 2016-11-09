#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-email
------------

Tests for `django-email` models module.
"""

from django.test import TestCase
from django_email import djemail


class EmailTest(TestCase):

    def test_send_email_system(self):
        mail = djemail.send_email(
            message="This is a message with no template or Context!",
            subject="My Subject"
        )
        self.assertEquals(mail, 1)

    def test_send_email_message(self):
        mail = djemail.send_email(
            to="email@test.com",
            message="This is a message with no template or Context!",
            subject="My Subject"
        )
        self.assertEquals(mail, 1)

    def test_send_email_message_list(self):
        mail = djemail.send_email(
            to=["email1@test.com", "email2@test.com"],
            message="This is a message with no template or Context!",
            subject="My Subject"
        )
        self.assertEquals(mail, 1)

    def test_send_email_message_tuple(self):
        mail = djemail.send_email(
            to=("email1@test.com", "email2@test.com"),
            message="This is a message with no template or Context!",
            subject="My Subject"
        )
        self.assertEquals(mail, 1)

    def test_send_email_context(self):
        mail = djemail.send_email(
            to="email@test.com",
            context={'content': 'This is a message'},
            subject="My Subject"
        )
        self.assertEquals(mail, 1)

    def test_send_email_template(self):
        mail = djemail.send_email(
            to="email@test.com",
            template="email/base",
            context={'variable': 'Variable Content'},
            subject="My Subject"
        )
        self.assertEquals(mail, 1)
