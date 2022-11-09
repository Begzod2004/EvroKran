from rest_framework import serializers
from apps.objects.models import Objects, ObjectImages


class ObjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectImages
        fields = ('id', 'image') 



class ObjectsSerializer(serializers.ModelSerializer):
    object_images = ObjectImagesSerializer(many=True)

    class Meta:
        model = Objects
        fields = (
            'id',
            'title',
            'category',
            'tonna',
            'size',
            'max_tonna',
            'lenght_strell',
            'speed_car',
            'description',
            'object_images',
        )

