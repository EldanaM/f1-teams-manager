from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import F1Team
from .serializers import F1TeamSerializer


@api_view(['POST', 'GET'])
def create_f1_team(request):
    if request.method == 'GET':
        teams = F1Team.objects.all()
        serializer = F1TeamSerializer(teams, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data.copy()
        if F1Team.objects.filter(name=data.get('name')).exists():
            return Response({"error": "Команда с таким именем уже существует!"}, 
                          status=400)
        
        
        if 'championships_won' in data and int(data['championships_won']) < 0:
            return Response({"error": "Чемпионств не может быть меньше 0!"}, 
                          status=400)
        
        serializer = F1TeamSerializer(data=data)
        if serializer.is_valid():
            team = serializer.save()
            return Response({
                "status": "success",
                "message": "Команда создана!",
                "team_id": team.id,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)