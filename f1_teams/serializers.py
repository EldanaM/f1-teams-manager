from rest_framework import serializers
from .models import F1Team

class F1TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = F1Team
        fields = '__all__'
    
    def validate_foundation_year(self, value):
        if value < 1950:
            raise serializers.ValidationError("Первая     Формула-1 была в 1950 году!")
        if value > 2024:
            raise serializers.ValidationError("Год из     будущего?")
        return value
    
class F1TeamSerializer(serializers.ModelSerializer):
        team_age = serializers.SerializerMethodField()
        
        class Meta:
            model = F1Team
            fields = '__all__'
        
        def get_team_age(self, obj):
            return 2024 - obj.foundation_year