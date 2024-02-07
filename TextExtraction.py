import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io
from SelectableTextOrNot import is_pdf_scanned
import cv2

def extract_text_combined(pdf_path):
    if is_pdf_scanned(pdf_path):
        images_ = extract_images_from_pdf(pdf_path)
        return extract_text_images(images_)
    else:
        return extract_text_selectable(pdf_path)
        

def extract_text_selectable(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    
    doc.close()
    return text

def extract_text_images(images):
    myconfig = r"--psm 6 --oem 3"
    text = ''
    for img in images:
        text += pytesseract.image_to_string(img,config=myconfig)
    return text

def extract_images_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Initialize an array to store images
    images = []

    # Iterate through all pages
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Convert the page to a pixmap
        pixmap = page.get_pixmap()

        # Convert the pixmap to a PIL Image
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        # Append the image to the array
        images.append(image)

    # Close the PDF document
    pdf_document.close()

    return images


