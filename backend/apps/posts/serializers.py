from rest_framework import serializers
from posts.models import Musician

class MusicianSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Musician
        fields = "__all__"