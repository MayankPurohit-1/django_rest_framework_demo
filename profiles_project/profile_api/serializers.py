from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializes name field"""
    fruit_name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }

