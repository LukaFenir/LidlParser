from typing import List

from PIL import Image
from pytesseract import pytesseract
from parsed_receipt import ParsedReceipt
import re


class ReceiptParser:
    def __init__(self, image_dir, tesseract_path):
        self.image_dir = image_dir
        self.tesseract_path = tesseract_path

    @staticmethod
    def correct_mistakes(text):
        return text.replace('@', '0').replace(' A', '').replace(' B', '').replace('Q0', '0')

    @staticmethod
    def trim_receipt(text):
        return re.split('[\n]*\*CUSTOMER COPY\* - PLEASE RETAIN RECEIPT', re.split('Copy[\n]*£[\n]*', text)[1])[0]

    @staticmethod
    def create_item_list(text):
        newline_list = text.split('\n')
        return list(filter(lambda item: (not '£' in item) and (not 'CARD' in item), newline_list))

    @staticmethod
    def create_parsed_receipt(item_list):
        total_string = item_list.pop()
        new_receipt = ParsedReceipt(item_list, total_string)
        return new_receipt

    def parse_and_touch_up(self, text):
        text_trimmed = self.trim_receipt(text)
        text_corrected = self.correct_mistakes(text_trimmed)
        # print(text_corrected[:-1])
        item_list: List[str] = self.create_item_list(text_corrected)
        parsed_receipt: ParsedReceipt = self.create_parsed_receipt(item_list)
        return parsed_receipt

    def parse_receipt(self, image_name):
        image_full_path = self.image_dir + image_name
        print('Image to be parsed: ' + image_full_path)

        image = Image.open(image_full_path)

        pytesseract.tesseract_cmd = self.tesseract_path

        text = pytesseract.image_to_string(image)
        return self.parse_and_touch_up(text)
