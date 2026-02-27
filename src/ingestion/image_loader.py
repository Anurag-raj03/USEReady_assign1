import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def load_image(file_path:str)->str:
    image=Image.open(file_path)
    return pytesseract.image_to_string(image)