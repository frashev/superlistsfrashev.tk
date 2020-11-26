from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # create an HttpRequest object
        request = HttpRequest()
        # pass this object to our home_page view, which gives us a response.
        response = home_page(request)
        # Then, we extract the .content of the response. These are the raw bytes,
        # the ones and zeros that would be sent down the wire to the user's browser.
        # We call .decode() to convert them into the string of HTML that's 
        # being sent to the user
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))


