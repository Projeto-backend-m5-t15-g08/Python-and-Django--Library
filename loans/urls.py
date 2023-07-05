from django.urls import path

from .views import LoanView

urlpatterns = [
    path("copy/<copy_id>/loan", LoanView.as_view()),
    # path("books/<book_id>/copy/<pk>", CopyDetailView.as_view()),
]
