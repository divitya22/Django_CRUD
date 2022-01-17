from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.name
