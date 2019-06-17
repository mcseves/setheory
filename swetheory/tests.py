from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, area_of_interest
from .models import AreaOfInterest

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class AreaOfInterestTests(TestCase):
    def setUp(self):
        AreaOfInterest.objects.create(name='Area')

    def test_AreaOfInterest_area_view_success_status_code(self):
        url = reverse('area_of_interest', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_AreaOfInterest_area_view_not_found_status_code(self):
        url = reverse('area_of_interest', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_AreaOfInterest_area_url_resolves_view(self):
        view = resolve('/area/1')
        self.assertEquals(view.func, area_of_interest)
