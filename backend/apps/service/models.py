from django.db import models

# Create your models here.


class Chronicle(models.Model):
    OPEN = 1
    CLOSED = 2
    STATUS_CHOICES = (
        ("Open", OPEN),
        ("Closed", CLOSED)
    )
    min_timestamp = models.DateTimeField()
    max_timestamp = models.DateTimeField()
    aircraft = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=OPEN)
    unique_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chronicle"
        verbose_name_plural = "Chronicles"


class Event(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    aircraft = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.unique_id}"

