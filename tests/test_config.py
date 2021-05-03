import pathlib


class TestConfig:
    IMAGE_DIRECTORY = str(pathlib.Path(__file__).parent.absolute()) + '\\test_input\\'

    TESSERACT_EXE_PATH = '<Path to Tesseract executable - see UB Mannheim>'
