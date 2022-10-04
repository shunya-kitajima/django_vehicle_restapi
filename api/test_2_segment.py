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


class AuthorizedSegmentApiTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="dummy", password="dummy_pw")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_2_1_should_get_all_segments(self):
        create_segment(segment_name="SUV")
        create_segment(segment_name="Sedan")
        res = self.client.get(SEGMENTS_URL)
        segments = Segment.objects.all().order_by("id")
        serializer = SegmentSerializer(segments, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


