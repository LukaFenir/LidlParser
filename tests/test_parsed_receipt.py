import unittest
from typing import List

from parsed_receipt import ParsedReceipt


class TestParsedReceipt(unittest.TestCase):

    def test_init(self):
        print('Testing: ParsedReceipt object creation')

    def test_parse_receipt_with_no_items(self):
        # Given
        items: List[str] = []
        total: str = ''

        # When
        parsed_receipt = ParsedReceipt(items, total)

        # Then
        self.assertEqual(parsed_receipt.total, 0.0)
        self.assertIsNotNone(parsed_receipt.items)
        self.assertEqual(len(parsed_receipt.items), 0)

    def test_parse_receipt_with_one_item(self):
        # Given
        items: List[str] = ['item1 1.00']
        total: str = 'TOTAL 0.99'

        # When
        parsed_receipt = ParsedReceipt(items, total)

        # Then
        self.assertEqual(parsed_receipt.total, 0.99)
        self.assertIsNotNone(parsed_receipt.items)
        self.assertEqual(len(parsed_receipt.items), 1)

    def test_parse_receipt_with_multiple_items(self):
        # Given
        items: List[str] = ['item1 1.00', 'item2 3.99', 'item3 2.01']
        total: str = 'TOTAL 0.99'

        # When
        parsed_receipt = ParsedReceipt(items, total)

        # Then
        self.assertEqual(parsed_receipt.total, 0.99)
        self.assertIsNotNone(parsed_receipt.items)
        self.assertEqual(len(parsed_receipt.items), 3)
        third_item = parsed_receipt.items[2]
        self.assertEqual(third_item.name, 'item3')
        self.assertEqual(third_item.price, 2.01)

    def test_parse_receipt_with_non_float_price(self):
        # Given
        items: List[str] = ['item1 P1.00']
        total: str = 'TOTAL 0.99'

        # Then
        with self.assertRaises(ValueError) as context:
            ParsedReceipt(items, total)
        self.assertEqual('Prices must be decimal numbers: could not convert string to float: \'P1.00\''
                         , str(context.exception))

    def test_parse_receipt_with_non_float_total(self):
        # Given
        items: List[str] = ['item1 1.00']
        total: str = 'TOTAL F0.99'

        # Then
        with self.assertRaises(ValueError) as context:
            ParsedReceipt(items, total)
        self.assertEqual('Total must be a decimal number: could not convert string to float: \'F0.99\''
                         , str(context.exception))

    def test_non_float_item_and_total(self):
        # Given
        items: List[str] = ['item1 G1.00']
        total: str = 'TOTAL F0.99'

        # Then
        with self.assertRaises(ValueError) as context:
            ParsedReceipt(items, total)
        self.assertEqual('Prices must be decimal numbers: could not convert string to float: \'G1.00\''
                         , str(context.exception))

    def test_some_non_float_items_and_total(self):
        # Given
        items: List[str] = ['item1 3.99', 'item2 G1.00']
        total: str = 'TOTAL F0.99'

        # Then
        with self.assertRaises(ValueError) as context:
            ParsedReceipt(items, total)
        self.assertEqual('Prices must be decimal numbers: could not convert string to float: \'G1.00\''
                         , str(context.exception))

    def test_unsplittable_invalid_item(self):
        # Given
        items: List[str] = ['item13.99']
        total: str = 'TOTAL 0.99'

        # Then
        with self.assertRaises(ValueError) as context:
            ParsedReceipt(items, total)
        self.assertEqual('Unable to parse item name and price from \'item13.99\''
                         , str(context.exception))
