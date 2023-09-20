from rest_framework import serializers
from .models import Musician

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = "__all__"