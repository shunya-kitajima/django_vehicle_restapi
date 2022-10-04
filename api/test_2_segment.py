from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Segment
from .serializers import SegmentSerializer

SEGMENTS_URL = "/api/segments"


def create_segment(segment_name):
    return Segment.objects.create(segment_name=segment_name)


def detail_url(segment_id):
    return reverse("api:segment-detail", args=[segment_id])

