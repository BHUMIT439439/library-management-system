import unittest
from selenium import webdriver

class LoginForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_form(self):
        # title test
        driver = self.driver
        driver.get("http://localhost:8000/login/")
        self.assertIn("Login", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
