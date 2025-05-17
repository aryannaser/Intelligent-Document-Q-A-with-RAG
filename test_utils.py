import unittest
from utils import extract_text_from_pdf

class TestPDFExtraction(unittest.TestCase):
    def test_extract_text_from_valid_pdf(self):
        # This test requires a sample PDF file in the documents/ directory
        try:
            with open('documents/sample.pdf', 'rb') as f:
                pdf_bytes = f.read()
            text = extract_text_from_pdf(pdf_bytes)
            self.assertIn('Page', text)  # Should contain at least one page marker
        except FileNotFoundError:
            self.skipTest('sample.pdf not found in documents/')

    def test_extract_text_from_invalid_bytes(self):
        text = extract_text_from_pdf(b'not a real pdf')
        self.assertIn('Error extracting text', text)

if __name__ == '__main__':
    unittest.main()
