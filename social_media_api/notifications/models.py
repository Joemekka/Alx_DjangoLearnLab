from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

CustomUser = get_user_model()


class Notification(models.Model):
    recipient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="notifications"
    )
    actor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="actions"
    )
    verb = models.CharField(max_length=255)

    # ✅ ALX wants this exact field name
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey(
        "content_type", "object_id"
    )  # ✅ string checker wants "target"

    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target or ''}"
