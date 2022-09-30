from django.db import models


class Segment(models.Model):
    segment_name = models.CharField(max_length=100)

    def __str__(self):
        return self.segment_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name


