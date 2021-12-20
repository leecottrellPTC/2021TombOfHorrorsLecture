from unittest.case import SkipTest
from django.test import TestCase
from django.urls import resolve
from tombApp.views import home_page
from django.http import HttpRequest, response
from tombApp.views import lore_page
from tombApp.views import character_page

# Create your tests here.
class HomePageTest(TestCase):

    #@unittest.skip('just because')
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page, "test.py - Home resolves incorrectly")

    def testHomePageH1(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Welcome to the Tomb of Horrors', html, 'H1 contents fail')

    def testMenuLinks(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('href="lore.html"', html, 'Link to lore.html not found')
        self.assertIn('href="home.html"', html, 'Link to home.html not found')

    def testLorepage(self):
        request = HttpRequest()
        response = lore_page(request)
        html = response.content.decode('utf')
        self.assertIn('Self-resetting traps were built into the plan', html, 'Lore page not complete')

    def testImageOnLore(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('src="/static/images/acererak.jpg"', html, 'tests.py - Acerak image not found')

    def testCharCreatePage(self):
        request = HttpRequest()
        response = character_page(request)
        html = response.content.decode('utf8')

        self.assertIn('<form method="post">', html, 'Form not on character page')
        self.assertIn('id="hitpoints"', html, 'Hitpoints id is not present on character page')
        self.assertIn('<input type="submit"', html, 'Submit button not on character page')

    def testHomePageContent(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('<b>doom</b>', html, 'Doom is not on home page contents')
