from djoser.email import ActivationEmail

class SujActivationEmail(ActivationEmail):
    template_name = "sujauth/mail.html"
