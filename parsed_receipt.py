import sys
from typing import List


class ParsedReceipt:

    def __init__(self, items: List[str], total: str):
        self.items: List[ParsedReceipt.ReceiptItem] = self.create_item_list(items)
        self.total: float = self.parse_total(total)

    @staticmethod
    def create_item_list(items: List[str]):
        item_list = []
        for item in items:
            split_string = tuple(item.rsplit(' ', 1))
            try:
                price = float(split_string[1])
                item_list.append(ParsedReceipt.ReceiptItem(split_string[0], price))
            except ValueError:
                error_message = sys.exc_info()[1]
                raise ValueError('Prices must be decimal numbers: ' + str(error_message))
            except IndexError:
                raise ValueError('Unable to parse item name and price from \'' + item + '\'')
        return item_list

    @staticmethod
    def parse_total(total):
        if 'TOTAL' in total:
            try:
                return float(total.rsplit(' ')[1])
            except ValueError:
                error_message = sys.exc_info()[1]
                raise ValueError("Total must be a decimal number: " + str(error_message))
        else:
            return 0.0

    class ReceiptItem:
        def __init__(self, name, price):
            self.name: str = name
            self.price: float = price



