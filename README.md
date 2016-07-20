**WELCOME TO DJANGO EMAIL**
=========================

Version: 0.1.2

Django email is a thin wrapper for django's multialternative email sending. For this you will need to specify a plain text template (.txt) and an html version (.html).
Django email takes your template and your context, renders it and sends the email, reducing the boilerplate required for sending an email.

We try to use defaults that make sense, but you can always adapt things to your needs. You can setup the subject, email from, email to and more.

Your templates must not have extension, but other than that we assume nothing.

Installation
------------

From PyPi packages via pip

```
  pip install django-email
  
```

How to use it
-------------

From a view:

```
    from django_email import email as djemail
    
    djemail.send_email(
        email_to="email@test.com",
        template_name="path/to/template", # .txt and/or .html
        context={'variable': 'Variable Content'},
        subject="My Subject"
    )

```
