from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    """Model definition for Message."""
    sending_date=models.DateTimeField(default=timezone.now)
    message=models.CharField(max_length=256)
    module_id=models.CharField(max_length=256)
    cheked=models.BooleanField(default=False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Message."""
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        return 'to '+ self.module_id

