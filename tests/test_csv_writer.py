import unittest
from unittest.mock import MagicMock

from parsed_receipt import ParsedReceipt

def some(file_path):

    with open(file_path) as f:
        return f.read()

class TestCsvWriter(unittest.TestCase):
    def test_writing_valid_receipt(self):
        # Given
        parsed_receipt: ParsedReceipt = ParsedReceipt(['item1 0.99'], 'TOTAL 0.99')
        writer = CsvWriter()

        # When
        writer.appendToCsv(parsed_receipt)

        # Then
        # Assert that file wrote successfully?
        # Mock?
        self.assertEqual()