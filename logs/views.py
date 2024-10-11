from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import LogEvent
from .serializers.logs_serializers import LogEventSerializer


@api_view(['GET'])
def get_logs(request) -> Response:
    logs = LogEvent.objects.all()
    serializer = LogEventSerializer(logs, many=True)
    return Response({"logs": serializer.data})


@api_view(['GET'])
def get_log_detail(request, log_id) -> Response:
    try:
        log = LogEvent.objects.get(id=log_id)
        serializer = LogEventSerializer(log)
        return Response(serializer.data)
    except LogEvent.DoesNotExist:
        return Response({"error": "Log not found"}, status=404)


@api_view(['POST'])
def create_log(request) -> Response:
    serializer = LogEventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
