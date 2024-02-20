# PDF Text Extraction and Categorization

This repository contains Python scripts for extracting text from PDF files, determining if the PDF is scanned or not, and categorizing the extracted text using a pre-trained model. The scripts utilize libraries such as PyMuPDF (fitz), pytesseract, PIL (Pillow), pandas, scikit-learn, nltk, and more.

## Files

- **TextExtraction.py**: Contains functions for extracting text from PDFs, both selectable and scanned.
- **SelectableTextOrNot.py**: Contains a function to determine if a PDF is scanned or not based on its content.
- **Model.py**: Contains functions for preprocessing text and predicting the category of extracted text using a pre-trained model.
- **Data Folder**: Contains a CSV file (`combined_data.csv`) with words and their corresponding categories, along with PDF files for testing the model.

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.

## Usage

1. Place PDF files you want to analyze in the `Data` folder.
2. Update the file paths in the scripts if necessary.
3. Run `Model.py` to extract text from PDFs and predict their categories.

## Example

```bash
python Model.py
```

## Note

- Ensure that Tesseract OCR is installed on your system for `pytesseract` to work correctly.
- The model assumes a pre-trained model is available for text categorization.

## Contributors

- Raghav Aloria raghavaloria@gmail.com
- Pranay Pandey pranaypandey2005@gmail.com
- Sarthak Sinha sarthaksinha2010@gmail.com
- Arpit Verma picarpitverma@gmail.com

Feel free to contribute to this project by forking and submitting a pull request.

---
