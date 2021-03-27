from django.db import models
import uuid


class Group(models.Model):
    group_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.first_name
