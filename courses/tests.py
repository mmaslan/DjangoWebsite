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

    def test_detail(self):
        response = self.client.get('/detail.html')
        self.assertTrue(response, 200)

    def test_list(self):
        response = self.client.get('/list.html')
        self.assertTrue(response, 200)

    def test_file(self):
        response = self.client.get('/file.html')
        self.assertTrue(response, 200)

    def test_image(self):
        response = self.client.get('/image.html')
        self.assertTrue(response, 200)

    def test_text(self):
        response = self.clinet.get('/text.html')
        self.assertTrue(response, 200)

    def test_video(self):
        response = client.get('/video.html')
        self.assertTrue(response, 200)