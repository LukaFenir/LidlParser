import unittest
from typing import List

from receipt_item import ReceiptItem
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
        receipt_items: List[ReceiptItem] = image_parser.parse_receipt(valid_receipt)
        print(receipt_items)

        #TODO Make object with TOTAL as a property
        receipt_items.pop()

        # Then
        self.assertIsNotNone(receipt_items)
        self.assertEqual(len(receipt_items), 34)
        #TODO
        # self.assertEqual(receipt_items.total, 41.91)
        self.assertEqual(receipt_items[0].name, "PF Compost 201")
        self.assertEqual(receipt_items[0].price, 0.99)

    # def test_invalid_receipt(self):


if __name__ == '__main__':
    unittest.main()
