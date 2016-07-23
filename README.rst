=============================
Django Email
=============================

.. image:: https://badge.fury.io/py/django-email.png
    :target: https://badge.fury.io/py/django-email

.. image:: https://travis-ci.org/swappsco/django-email.png?branch=master
    :target: https://travis-ci.org/swappsco/django-email

Django Email Templates made easy

Current Version 0.1.6

Django email is a thin wrapper for django's multialternative email sending. For this you will need to specify a plain text template (.txt) and an html version (.html). Django email takes your template and your context, renders it and sends the email, reducing the boilerplate required for sending an email.

We try to use defaults that make sense, but you can always adapt things to your needs. You can setup the subject, email from, email to and more.

Your templates must not have extension, but other than that we assume nothing.


Quickstart
----------

Install Django Email::

    pip install django-email

Then use it in a project::

    from django_email import email as djemail

    # Simple Usage
    # Admin will receive a message
    djemail.send_mail(message="My Message", subject="The Subject")

    # Send an email to a specific email
    djemail.send_mail(
	    to="email@test.com",
	    message="My Message",
	    subject="The Subject")

    # Advanced Usage
    djemail.send_email(
        to="email@test.com",
        template_name="path/to/template", # .txt and/or .html
        context={'variable': 'Variable Content'},
        subject="My Subject"
    )


Features
--------

* Send easy email to ADMINS.
* Send TXT/HTML Email using a predefined template.
* Send Email using your own custom templates. 

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
