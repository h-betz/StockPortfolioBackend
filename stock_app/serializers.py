from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=50)


    def create(self, validated_data):
        """
        Create and return a new `Stock` instance, given the validated data.
        """
        return Stock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Stock' instance, given the validated data
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Stock
        #fields = ('ticker','volume')   returns only volume and ticker
        fields = '__all__'   #returns everything
        