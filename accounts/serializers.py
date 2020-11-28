from rest_framework import serializers
from accounts import models


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwarg = {'password': {'write_only': True, 'input_type': 'password'}}

    def create(self, validated_data):
        """ Create and return new user """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


# class ProfileFeedItemSerializer(serializers.ModelSerializer):
#     """ serializes profile feed items """
#
#     class Meta:
#         model = models.ProfileFeedItem
#         fields = ('id', 'user_profile', 'status_text', 'created_on')
#         exta_kwargs = {'user_profile': {'write_only': True}}
