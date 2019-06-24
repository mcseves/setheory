from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import *
from .models import *
from .forms import *


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

    def test_AreaOfInterest_area_view_contains_navigation_links(self):
        area_url = reverse('area_of_interest', kwargs={'name': "Area"})
        homepage_url = reverse('home')
        new_theory_url = reverse('new_theory', kwargs={'name': "Area"})

        response = self.client.get(area_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_theory_url))


class NewAreaOfInterestTests(TestCase):
    def setUp(self):
        AreaOfInterest.objects.create(name='Area')
        # User.objects.create_user(username='john', email='john@doe.com', password='123')

    def test_new_theory_view_success_status_code(self):
        url = reverse('new_theory', kwargs={'name': "Area"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_theory_view_not_found_status_code(self):
        url = reverse('new_theory', kwargs={'name': "donut"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_theory_url_resolves_new_theory_view(self):
        view = resolve('/area/Area/new/')
        self.assertEquals(view.func, new_theory)

    def test_view_contains_link_back_to_view(self):
        new_topic_url = reverse('new_theory', kwargs={'name': "Area"})
        area_url = reverse('area_of_interest', kwargs={'name': "Area"})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(area_url))

    def test_csrf(self):
        url = reverse('new_theory', kwargs={'name': "Area"})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')
    #
    # def test_new_theory_valid_data(self):
    #     url = reverse('new_theory', kwargs={'name': "Area"})
    #     data = {
    #         'name': 'Test'
    #     }
    #     response = self.client.post(url, data)
    #     self.assertTrue(Construct.objects.exists())
    #
    # def test_new_theory_invalid_data(self):
    #     url = reverse('new_theory', kwargs={'name': "Area"})
    #     response = self.client.post(url, {})
    #     form = response.context.get('form')
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTrue(form.errors)
    #
    # def test_new_theory_invalid_data_empty_fields(self):
    #     url = reverse('new_theory', kwargs={'name': "Area"})
    #     data = {
    #         'name': ''
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertFalse(Construct.objects.exists())
    #
    # def test_contains_form(self):
    #     url = reverse('new_theory', kwargs={'name': "Area"})
    #     response = self.client.get(url)
    #     form = response.context.get('form')
    #     self.assertIsInstance(form, NewTheoryForm)
