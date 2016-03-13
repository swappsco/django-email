**WELCOME TO DJANGO EMAIL**
=========================

Django email is a thin wrapper for django's multialternative email sending. For this you will need to specify a plain text template (.txt) and an html version (.html).
Django email takes your template and your context, renders it and sends the email, reducing the boilerplate required for sending an email.

We try to use defaults that make sense, but you can always adapt things to your needs. You can setup the subject, email from, email to and more.

Your templates must be under 'email/' and have not extension, but other than that we assume nothing.
