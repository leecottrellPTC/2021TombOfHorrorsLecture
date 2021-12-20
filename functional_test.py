from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import requests
class FunctionalTest(unittest.TestCase):
    def setUp(self):
        #chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.headless = True
        self.browser = webdriver.Chrome()
       # self.browser = webdriver.Chrome(options=chromeOptions)
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    @unittest.skip('Just because')
    def test_title(self):
        #self.assertIn('Django', self.browser.title, 'Functional test - test title - Wrong title')
        #refactored 12-3 to add proper title after writing template
        self.assertIn('Tomb of Horror', self.browser.title, 'Functional test - test title - Wrong title')

    
    def testLink(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_partial_link_text("Lore").click()
        self.assertIn('Lore', self.browser.title, 'Functional test - Lore Link does not go to correct page')
    
    def testActiveLink(self):
        self.browser.get('http://localhost:8000/lore.html')
        #self.browser.find_element_by_partial_link_text("Lore").click()
        loreCSS = self.browser.find_element_by_partial_link_text("Lore")
        #self.assertIn('Lore', self.browser.title, 'Functional test - lore title')
        cssClass = loreCSS.get_attribute('class')
        self.assertIn('active', cssClass, 'Functional - Active class not found')

    
    def testChar(self):
        self.browser.get('http://localhost:8000/character.html')
        self.browser.find_element_by_id("charname").send_keys("Kaladin")
        self.browser.find_element_by_id("hitpoints").send_keys("60")
        self.browser.find_element_by_id("armor").send_keys("15")
        self.browser.find_element_by_id("submit").click()

        self.assertIn('Kaladin', self.browser.title, 'Fun - name not in title')
        hp = self.browser.find_element_by_id("hp")
        self.assertEqual("60", hp.text, "Fun - HP is incorrect")
        ac = self.browser.find_element_by_id("ac")
        self.assertEqual("15", ac.text, "Fun - AC is incorrect")

    def testGloblChar(self):
        self.browser.get('http://localhost:8000/character.html')
        self.browser.find_element_by_id("charname").send_keys("Kaladin")
        self.browser.find_element_by_id("hitpoints").send_keys("60")
        self.browser.find_element_by_id("armor").send_keys("15")
        self.browser.find_element_by_id("submit").click()

        self.browser.get('http://localhost:8000/home.html')
        h1 = self.browser.find_element_by_xpath("/html/body/h1").text
        self.assertIn('Kaladin', h1)

    def testCSSFileLoads(self):
        resp = requests.head('http://localhost:8000/static/darkly.css')
        self.assertEqual(200, resp.status_code, 'darkly.css does not load')
        
if __name__ == '__main__':
    unittest.main()
    