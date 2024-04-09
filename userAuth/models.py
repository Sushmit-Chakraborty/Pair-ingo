from django.conf import settings
from django.db import models

class Technology(models.Model):
    userTech = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    technology = models.CharField(max_length=100,null=True)