from rest_framework import serializers
from .models import Musician

class MusicianSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Musician
        fields = "__all__"