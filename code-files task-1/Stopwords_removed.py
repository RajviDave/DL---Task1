import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
stop_words = set(stopwords.words('english'))

df = pd.read_excel('C:/Users/RAJVI DAVE/OneDrive/Desktop/Sem 6/DL/Task1/Combined_Abstracts.xlsx', engine='openpyxl')

def remove_stopwords(text):
     words = word_tokenize(text)
     filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]
     return ' '.join(filtered_words)

df['Cleaned_Abstract'] = df['Combined_Abstract'].apply(remove_stopwords)

df.to_excel('cleaned_combined_Abstract.xlsx', index=False)
