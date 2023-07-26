from rest_framework import serializers
from .models import Rating
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']
        validators = [
            UniqueTogetherValidator(
                queryset = Rating.objects.all(),
                fields = ['user', 'menuitem_id', 'rating']
            )
        ]
        extra_kwargs = {
            'rating': {
                'max_value': 5,
                'min_value': 0,
            }
        }
