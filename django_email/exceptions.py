class EmailTemplateNotFound(Exception):
    def __init__(self, arg):
        self.msg = arg


class MailServerException(Exception):
    def __init__(self, arg):
        self.msg = arg
