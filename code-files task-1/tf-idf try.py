# tokenising
import pandas as pd
df = pd.read_excel("C:/Users/RAJVI DAVE/OneDrive/Desktop/Sem 6/DL/Task1/cleaned_combined_Abstract.xlsx")

df['Tokens'] = df['Cleaned_Abstract'].apply(lambda x: str(x).split())

# print(df[['Researcher', 'Tokens']].head())

from collections import Counter

def compute_tf(tokens):
    total_tokens = len(tokens)
    token_counts = Counter(tokens)
    tf = {word: count / total_tokens for word, count in token_counts.items()}
    return tf

df["TF"] = df["Tokens"].apply(compute_tf)

print(df[["Researcher", "TF"]])