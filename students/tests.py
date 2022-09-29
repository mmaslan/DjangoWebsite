from django.test import TestCase


class URLTest(TestCase):
    def test_details(self):
        response = self.client.get('/details.html')
        self.assertTrue(response, 200)

    def test_list(self):
        response = self.client.get('/list.html')
        self.assertTrue(response, 200)

    def test_registration(self):
        response = self.client.get('/registration.html')
        self.assertTrue(response, 200)