import fitz
import pytesseract
from PIL import Image

def extract_text_from_pdf(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""

        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            
            # Extract text from page
            text += page.get_text()

        return text

    except Exception as e:
        print(f"Error while extracting text from PDF: {e}")
        return None

def is_pdf_scanned(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        has_text = False
        has_images = False

        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]

            # Check for text
            if page.get_text("text") != "":
                has_text = True

            # Check for images
            image_list = page.get_images(full=True)
            if image_list:
                has_images = True

            # Check OCR on images
            for img_index, img_info in enumerate(image_list):
                try:
                    img_index = img_info[0]
                    base_image = pdf_document.extract_image(img_index)
                    image_bytes = base_image["image"]
                    image = Image.frombytes("RGB", base_image["size"], image_bytes)
                    
                    # Perform OCR with English language
                    text_from_image = pytesseract.image_to_string(image, lang='eng')

                    if text_from_image.strip():
                        has_text = True
                except Exception as img_error:
                    # print(f"Error processing image: {img_error}")
                    continue

        return has_images and not has_text

    except Exception as e:
        return False

if __name__ == "__main__":
    mypdf = r"Data/patient-record.pdf"
    result = is_pdf_scanned(mypdf)
    print(result)
