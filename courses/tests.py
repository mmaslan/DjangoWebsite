from django.test import TestCase


class URLTest(TestCase):
    def test_base(self):
        response = self.client.get('/base.html')
        self.assertTrue(response, 200)

    def test_login(self):
        response = self.client.get('/login.html')
        self.assertTrue(response, 200)

    def test_logged_out(self):
        response = self.client.get('/logged_out.html')
        self.assertTrue(response, 200)