from django.db import models


class AbsCreated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbsActive(models.Model):
    """
    Модель, помогающая отследить активность объекта.
    """

    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        abstract = True