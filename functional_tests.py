from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notives the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

# this clause -- this is how a Python script checks
# if it has been executed from the command line
# We call unittest.main(), which launches the unittest test runner
if __name__ == '__main__':
        unittest.main()









