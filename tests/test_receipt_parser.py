import unittest
from typing import List

from parsed_receipt import ParsedReceipt
from receipt_parser import ReceiptParser
from tests.test_config import TestConfig


class TestReceiptParser(unittest.TestCase):
    def test_valid_receipt(self):
        """
        Test that a Lidl receipt can be parsed
        """
        # Given
        image_parser = ReceiptParser(TestConfig.IMAGE_DIRECTORY, TestConfig.TESSERACT_EXE_PATH)
        valid_receipt = "valid_lidl_receipt.jpg"

        # When
        parsed_receipt: ParsedReceipt = image_parser.parse_receipt(valid_receipt)
        receipt_items: List[ParsedReceipt.ReceiptItem] = parsed_receipt.items
        print(receipt_items)

        # Then
        self.assertEqual(parsed_receipt.total, 41.91)
        self.assertIsNotNone(receipt_items)
        self.assertEqual(len(receipt_items), 34)
        self.assertEqual(receipt_items[0].name, "PF Compost 201")
        self.assertEqual(receipt_items[0].price, 0.99)

    # def test_invalid_receipt(self):
