from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']

class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()  # Nesting the BreedSerializer to show full breed details in the dog response

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']
