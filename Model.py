from PIL import Image
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from TextExtraction import extract_text_combined

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

def predict_category_from_text(extracted_text, model, combined_df_path):
    try:
        # Load the combined CSV file
        combined_df = pd.read_csv(combined_df_path)

        # Handling NaN values
        combined_df = combined_df.dropna().reset_index(drop=True)

        if combined_df.empty:
            print("The CSV file is empty. Further processing cannot be done.")
            return None
        else:
            # Text preprocessing
            combined_df['word'] = combined_df['word'].apply(preprocess_text)

            # Create a TF-IDF model with SVM classifier
            model = make_pipeline(TfidfVectorizer(), SVC())

            # Train the model
            X = combined_df['word']
            y = combined_df['category']
            model.fit(X, y)

            # Preprocess the extracted text
            preprocessed_text = preprocess_text(extracted_text)

            # Use the model to predict the category
            predicted_category = model.predict([preprocessed_text])[0]
            # print(f'******************The preprocessed text belongs to the category: {predicted_category}******************')
            return predicted_category

    except pd.errors.EmptyDataError:
        print("The CSV file is empty. Further processing cannot be done.")
        return None
    except Exception as e:
        print(f"Error during data processing: {e}")
        return None
    
#example test case
    
if __name__ == '__main__':
    mypdf = r"Data\8.pdf"
    mydata = r"Data\combined_data.csv"
    text = extract_text_combined(mypdf)
    category = predict_category_from_text(text, model=None, combined_df_path=mydata)
    print(category)
