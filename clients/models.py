from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_created=True)


class Company(models.Model):
    name = models.CharField(max_length=255)
    vatid = models.CharField(blank=True, max_length=10)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
