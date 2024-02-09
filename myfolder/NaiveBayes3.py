from PIL import Image
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import os
from TextExtraction import extract_text_combined  # Assuming you have a module named TextExtraction for text extraction

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

def load_data_from_folders(data_folder):
    data = {'word': [], 'category': []}
    categories = os.listdir(data_folder)

    for category in categories:
        category_path = os.path.join(data_folder, category)
        if os.path.isdir(category_path):
            pdf_files = [f for f in os.listdir(category_path) if f.endswith('.pdf')]
            category_text = ""

            for pdf_file in pdf_files:
                pdf_path = os.path.join(category_path, pdf_file)
                text = extract_text_combined(pdf_path)
                category_text += text + " "

            data['word'].append(category_text)
            data['category'].append(category)

    return pd.DataFrame(data)

def train_model(data, model_path):
    try:
        # Handling NaN values
        data = data.dropna().reset_index(drop=True)

        if data.empty:
            print("The data is empty. Model cannot be trained.")
            return None
        else:
            # Text preprocessing
            data['word'] = data['word'].apply(preprocess_text)

            # Create a TF-IDF model with SVM classifier
            model = make_pipeline(TfidfVectorizer(), SVC())

            # Train the model
            X = data['word']
            y = data['category']
            model.fit(X, y)

            # Save the trained model
            joblib.dump(model, model_path)

            print("Model trained successfully.")
            return model

    except pd.errors.EmptyDataError:
        print("The data is empty. Model cannot be trained.")
        return None
    except Exception as e:
        print(f"Error during data processing: {e}")
        return None

if __name__ == '__main__':
    # Paths
    pdf_folder = "Data/PDFs"  # Update with the actual path to your PDF folder
    combined_data_path = "Data/combined_data.csv"
    trained_model_path = "Data/trained_model.joblib"

    # Load data from PDF folders
    data = load_data_from_folders(pdf_folder)

    # Save the combined data to a CSV file
    data.to_csv(combined_data_path, index=False)

    # Train the model
    trained_model = train_model(data, trained_model_path)

    # Example: Predict category for a new PDF
    if trained_model:
        new_pdf_path = "Data/new_patient_record.pdf"  # Update with the actual path to your new PDF
        new_text = extract_text_combined(new_pdf_path)
        predicted_category = trained_model.predict([preprocess_text(new_text)])[0]
        print(f'The preprocessed text belongs to the category: {predicted_category}')
