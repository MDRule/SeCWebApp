from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']

class DogSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())  # Use the breed ID directly

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy', 'owner']

