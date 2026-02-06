from django.db import models

class F1Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    foundation_year = models.IntegerField()
    championships_won = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name