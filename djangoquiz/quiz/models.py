from django.db import models
from django.db.models import CharField


class QuesModel(models.Model):
    question = CharField(max_length=200, null=True)
    op1 = CharField(max_length=200, null=True)
    op2 = CharField(max_length=200, null=True)
    op3 = CharField(max_length=200, null=True)
    op4 = CharField(max_length=200, null=True)
    ans = CharField(max_length=200, null=True)

    def __str__(self):
        return self.question
