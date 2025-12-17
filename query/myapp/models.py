from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=20)
    faculty = models.ManyToManyField(Faculty)

    def __str__(self):
        return self.name
