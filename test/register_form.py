import unittest
from selenium import webdriver

class RegisterForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_register_form(self):
        # title test
        driver = self.driver
        driver.get("http://localhost:8000/register/")
        self.assertIn("Register", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
