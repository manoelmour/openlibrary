
import unittest
from unittest.mock import patch, MagicMock

def notfound(config, i, is_valid_url, read_file, web):
    if (
        config.default_image
        and i.default.lower() != "false"
        and not is_valid_url(i.default)
    ):
        return read_file(config.default_image)
    elif is_valid_url(i.default):
        return web.seeother(i.default)
    else:
        return web.notfound("")

class MockWeb:
    def seeother(self, url):
        return f"Redirect to {url}"
    
    def notfound(self, message):
        return "Not found"

class TestNotfound(unittest.TestCase):
    def setUp(self):
        self.config = MagicMock()
        self.i = MagicMock()
        self.is_valid_url = MagicMock()
        self.read_file = MagicMock()
        self.web = MockWeb()

    def test_case_1(self):
        self.config.default_image = "image_path"
        self.i.default = "true"
        self.is_valid_url.return_value = False
        self.read_file.return_value = "File content"

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "File content")

    def test_case_2(self):
        self.config.default_image = "image_path"
        self.i.default = "true"
        self.is_valid_url.return_value = True

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "Redirect to true")

    def test_case_3(self):
        self.config.default_image = "image_path"
        self.i.default = "false"
        self.is_valid_url.return_value = False

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "Not found")

    def test_case_4(self):
        self.config.default_image = "image_path"
        self.i.default = "false"
        self.is_valid_url.return_value = True

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "Redirect to false")

    def test_case_5(self):
        self.config.default_image = None
        self.i.default = "true"
        self.is_valid_url.return_value = False

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "Not found")

    def test_case_6(self):
        self.config.default_image = None
        self.i.default = "true"
        self.is_valid_url.return_value = True

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "Redirect to true")

    def test_case_7(self):
        self.config.default_image = None
        self.i.default = "false"
        self.is_valid_url.return_value = False

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "Not found")

    def test_case_8(self):
        self.config.default_image = None
        self.i.default = "false"
        self.is_valid_url.return_value = True

        result = notfound(self.config, self.i, self.is_valid_url, self.read_file, self.web)
        self.assertEqual(result, "Redirect to false")

if __name__ == '__main__':
    unittest.main()