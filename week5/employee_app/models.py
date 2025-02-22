from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.emp_id} - {self.name}"
