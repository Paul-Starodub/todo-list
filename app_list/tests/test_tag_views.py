from django.test import TestCase
from django.urls import reverse

from app_list.models import Tag

TAG_URL = reverse("app_list:tag-list")


class FixtureListTests(TestCase):
    def test_get_fixture_data(self):
        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(list(response.context["tag_list"]), [])
        self.assertEqual(len(list(response.context["tag_list"])), 3)


class OwnTagsTests(TestCase):
    def test_get_fixture_data(self):
        Tag.objects.create(name="Tag with name...")
        all_tags = Tag.objects.all()
        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual((list(response.context["tag_list"])), list(all_tags))
