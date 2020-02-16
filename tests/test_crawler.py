import unittest
from crawler import Parser


class CrawlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = '../samples/sample-0-origin.html'
        self.xpath = '//div[@class="panel-body"]/*[normalize-space(text()) = "Make everything OK"]'

    def clean_element_text(self, element):
        if hasattr(element, 'text'):
            return element.text.strip()

    def test_local_file_crawler(self):
        parser = Parser('file', self.xpath, file_path=self.file_path)
        data = self.clean_element_text(parser.parse())
        self.assertEqual(data, "Make everything OK", "Result should be `Make everything OK`")

    def test_parse_file1(self):
        file_path = '../samples/sample-1-evil-gemini.html'
        parser = Parser('file', self.xpath, file_path=file_path)
        data = self.clean_element_text(parser.parse())
        self.assertEqual(data, "Make everything OK", "Result should be `Make everything OK`")

    def test_parse_file2(self):
        file_path = '../samples/sample-2-container-and-clone.html'
        parser = Parser('file', self.xpath, file_path=file_path)
        data = self.clean_element_text(parser.parse())
        self.assertEqual(data, "Make everything OK", "Result should be `Make everything OK`")

    def test_parse_file3(self):
        file_path = '../samples/sample-3-the-escape.html'
        parser = Parser('file', self.xpath, file_path=file_path)
        data = self.clean_element_text(parser.parse())
        self.assertEqual(data, "Make everything OK", "Result should be `Make everything OK`")

    def test_parse_file4(self):
        file_path = '../samples/sample-4-the-mash.html'
        parser = Parser('file', self.xpath, file_path=file_path)
        data = self.clean_element_text(parser.parse())
        self.assertEqual(data, "Make everything OK", "Result should be `Make everything OK`")


if __name__ == "__main__":
    unittest.main()
