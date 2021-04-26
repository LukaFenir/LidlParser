from PIL import Image
from pytesseract import pytesseract
from receipt_item import ReceiptItem


class ReceiptParser:
    def __init__(self, image_dir, tesseract_path):
        self.image_dir = image_dir
        self.tesseract_path = tesseract_path

    @staticmethod
    def correct_mistakes(text):
        return text.replace('@', '0').replace(' A', '').replace(' B', '')

    @staticmethod
    def trim_receipt(text):
        return text.split('Copy\n\n£\n')[1].split('\n\n*CUSTOMER COPY* - PLEASE RETAIN RECEIPT')[0]

    @staticmethod
    def create_item_list(text):
        newline_list = text.split('\n')
        return list(filter(lambda item: not ' x ' in item, newline_list))

    @staticmethod
    def create_item_dictionary(item_list):
        new_list = []
        for item in item_list:
            split_string = tuple(item.rsplit(' ', 1))
            new_list.append(ReceiptItem(split_string[0], split_string[1]))
        return new_list

    def process_to_dictionary(self, text):
        text_trimmed = self.trim_receipt(text)
        text_corrected = self.correct_mistakes(text_trimmed)
        # print(text_corrected[:-1])
        item_list = self.create_item_list(text_corrected)
        item_dictionary = self.create_item_dictionary(item_list)
        print(item_dictionary)

    def parse_receipt(self, image_name):
        image_full_path = self.image_dir + image_name
        print('Image to be parsed: ' + image_full_path)

        image = Image.open(image_full_path)

        pytesseract.tesseract_cmd = self.tesseract_path

        text = pytesseract.image_to_string(image)
        self.process_to_dictionary(text)
