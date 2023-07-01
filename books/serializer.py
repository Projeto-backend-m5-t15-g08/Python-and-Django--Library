from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255, default=None)
    publisher = serializers.CharField(max_length=50)
    published_at = serializers.DateTimeField(read_only=True)
    active_loan = serializers.BooleanField(default=False)
    user_id = serializers.IntegerField()

    def create(self, validated_data: dict):
        return Book.objects.create(**validated_data)
