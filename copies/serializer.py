from rest_framework import serializers


class CopySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    quantity = serializers.IntegerField()
    book_id = serializers.IntegerField()
