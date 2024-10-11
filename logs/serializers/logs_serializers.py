from rest_framework import serializers

from ..models import LogEvent


class LogEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEvent
        fields = '__all__'
        read_only_fields = ['timestamp']
