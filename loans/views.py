from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
)

from loans.models import Loan
from loans.serializers import LoanSerializer
from rest_framework.views import status, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsColaborator
from copies.models import Copy


class LoanView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]

    queryset = Loan
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        copy_id = kwargs["copy_id"]

        copy = Copy.objects.get(id=copy_id)

        if copy.active_loan:
            return Response(
                {"message": "Livro já alugado."},
                status=status.HTTP_201_CREATED,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return_data = serializer.data
        return_data["return_date"] = serializer.data["return_date"][:10]

        return Response(
            return_data, status=status.HTTP_201_CREATED, headers=headers
        )


class LoanDetailView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsColaborator]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
