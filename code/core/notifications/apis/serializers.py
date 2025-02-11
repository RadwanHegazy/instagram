from notifications.models import Notification
from rest_framework import serializers


class GetNotificationSerializer (serializers.ModelSerializer) : 

    class Meta:
        model = Notification
        fields = "__all__"

