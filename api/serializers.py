from rest_framework import serializers
from django.contrib.auth.models import User
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_Data):
        print(validated_Data)
        user = User.objects.create(
            **validated_Data
        )
        user.save()
        return user