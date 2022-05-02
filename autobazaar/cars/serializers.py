from rest_framework import serializers

from .models import Car


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'category', 'brand', 'carModel',
                  'description', 'year_of_issue')


class CarDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Car
        exclude = ("sold", )
