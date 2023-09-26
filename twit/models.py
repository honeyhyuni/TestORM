from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + self.last_name


class Tweet(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
