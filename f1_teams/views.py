from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import F1Team
from .serializers import F1TeamSerializer


@api_view(['POST'])
def create_f1_team(request):
    if request.method == 'POST':
        serializer = F1TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)