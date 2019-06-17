from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, area_of_interest, new_theory
from .models import AreaOfInterest

class HomeTests(TestCase):
    def setUp(self):
        self.area = AreaOfInterest.objects.create(name='area teste')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        area_of_interest_url = reverse('area_of_interest', kwargs={'name': self.area.name})
        self.assertContains(self.response, 'href="{0}"'.format(area_of_interest_url))


class AreaOfInterestTests(TestCase):
    def setUp(self):
        AreaOfInterest.objects.create(name='Area')

    def test_AreaOfInterest_area_view_success_status_code(self):
        url = reverse('area_of_interest', kwargs={'name': "Area"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_AreaOfInterest_area_view_not_found_status_code(self):
        url = reverse('area_of_interest', kwargs={'name': "donuts"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_AreaOfInterest_area_url_resolves_view(self):
        view = resolve('/area/Area')
        self.assertEquals(view.func, area_of_interest)

    def test_AreaOfInterest_area_view_contains_link_back_to_homepage(self):
        area_url = reverse('area_of_interest', kwargs={'name': "Area"})
        response = self.client.get(area_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))


class NewTheoryTests(TestCase):
    def setUp(self):
        AreaOfInterest.objects.create(name='Area')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_theory', kwargs={'name': "Area"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_theory', kwargs={'name': "donut"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/area/Area/new/')
        self.assertEquals(view.func, new_theory)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_theory', kwargs={'name': "Area"})
        area_url = reverse('area_of_interest', kwargs={'name': "Area"})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(area_url))
