from apps.models import Model


class Loan(Model):
    __table__ = 'loan'
    __primary_key__ = 'loanid'
