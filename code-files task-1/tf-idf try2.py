import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import re

df = pd.read_excel('C:/Users/RAJVI DAVE/OneDrive/Desktop/Sem 6/DL/Task1/cleaned_combined_Abstract.xlsx')

# Clean and tokenize abstracts (you can improve this with NLP tools)
def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.split()

df['tokens'] = df['Abstract'].apply(preprocess)