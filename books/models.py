from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=255, null=True)
    publisher = models.CharField(max_length=50, null=False)
    published_at = models.DateTimeField(auto_now_add=True)
    active_loan = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="book"
    )
