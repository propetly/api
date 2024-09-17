from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    agency = models.ForeignKey("agencies.Agency", on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return f"{self.last_name} {self.first_name} <{self.email}>"
