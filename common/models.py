from django.db import models


class LogicalDeleteModel(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TrackedModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    date_last_updated = models.DateTimeField(auto_now=True, verbose_name='Date last updated')

    class Meta:
        abstract = True
