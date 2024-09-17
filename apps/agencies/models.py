from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    watermark = models.CharField(max_length=255, blank=True, null=True)

    director_first_name = models.CharField(max_length=255, blank=True, null=True)
    director_last_name = models.CharField(max_length=255, blank=True, null=True)
    director_middle_name = models.CharField(max_length=255, blank=True, null=True)
    director_email = models.EmailField(blank=True, null=True)
    director_phone = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
