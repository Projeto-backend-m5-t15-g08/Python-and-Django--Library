from rest_framework import serializers


class LoanSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    copy_id = serializers.IntegerField(read_only=True)
    loaned_by = serializers.ReadOnlyField(source="user.email")
