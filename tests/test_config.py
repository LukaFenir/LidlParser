import pathlib


class TestConfig:
    IMAGE_DIRECTORY = str(pathlib.Path(__file__).parent.absolute()) + '\\test_input\\'

    TESSERACT_EXE_PATH = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'
