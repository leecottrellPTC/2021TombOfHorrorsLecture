from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
class FunctionalTest(unittest.TestCase):
    def setUp(self):
        #chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.headless = True
        self.browser = webdriver.Chrome()
       # self.browser = webdriver.Chrome(options=chromeOptions)
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        #self.assertIn('Django', self.browser.title, 'Functional test - test title - Wrong title')
        #refactored 12-3 to add proper title after writing template
        self.assertIn('Tomb of Horror', self.browser.title, 'Functional test - test title - Wrong title')
    
    def testLink(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_partial_link_text("Lore").click()
        self.assertIn('Lore', self.browser.title, 'Functional test - Lore Link does not go to correct page')
    
    def testActiveLink(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_partial_link_text("Lore").click()
        loreCSS = self.browser.find_element_by_partial_link_text("Lore")
        #self.assertIn('Lore', self.browser.title, 'Functional test - lore title')
        cssClass = loreCSS.get_attribute('class')
        self.assertIn('active', cssClass, 'Functional - Active class not found')
       


if __name__ == '__main__':
    unittest.main()
    