from rest_framework import serializers
from . import models

class TypingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypingResponse
        exclude = ["UserName"]

