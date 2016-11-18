from django.db.models import Model, CharField


class Ad(Model):
    title   = CharField(max_length=128)
    content = CharField(max_length=512)
