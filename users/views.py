from rest_framework.generics import (
    CreateAPIView,
)

from users.models import User
from users.serializers import UserSerializer


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
