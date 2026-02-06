from rest_framework import serializers
from .models import F1Team

class F1TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = F1Team
        fields = '__all__'
    
    def validate_foundation_year(self, value):
        if value < 1950:
            raise serializers.ValidationError("Ф1 только с 1950 года!")
        return value