from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from loans.models import Loan
from loans.serializers import LoanSerializer
from rest_framework.views import status, Response


from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsColaborator


class LoanView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]

    queryset = Loan
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return_data = serializer.data
        return_data["return_date"] = serializer.data["return_date"][:10]

        return Response(return_data, status=status.HTTP_201_CREATED, headers=headers)
