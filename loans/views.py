from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from loans.models import Loan
from loans.serializers import LoanSerializer


from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsColaborator


class LoanView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]

    queryset = Loan
    serializer_class = LoanSerializer
