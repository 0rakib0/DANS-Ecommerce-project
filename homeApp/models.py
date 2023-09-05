from django.db import models

# Create your models here.


class Massage(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    message = models.TextField()
    isRed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
