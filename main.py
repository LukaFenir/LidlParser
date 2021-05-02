from config import Config
from receipt_parser import ReceiptParser
from parsed_receipt import ParsedReceipt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_parser = ReceiptParser(Config.IMAGE_DIRECTORY, Config.TESSERACT_EXE_PATH)
    parsed_receipt: ParsedReceipt = image_parser.parse_receipt('2021.04.17_1300141322021041745888.jpg')

    print(parsed_receipt.items[0].name + ": " + str(parsed_receipt.items[0].price))
