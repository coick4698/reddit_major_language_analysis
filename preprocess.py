import pandas as pd
import os
import re
import nltk
from nltk.corpus import stopwords

"""
- AI used
- exclude stopwords which are already organized in library
"""
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
custom_stopwords = ['im','like','would','know','one','get','think','dont','people','could',
                    'also','ive','something','want','school','even','good','way']
stop_words.update(custom_stopwords)

"""
- convert to the lowercase letters
- delete URL
- delete special characters
- return pure text
"""
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text

# tokenize text
def tokenize(text):
    tokens = text.split()
    return [t for t in tokens if t not in stop_words and len(t) > 1]

"""
- AI used
- load preprocess
- normalize complex posts into unified text entries
"""
def load_and_preprocess_all(data_dir="data"):
    dfs = []
    for filename in os.listdir(data_dir):
        if filename.endswith("_posts.csv"):
            path = os.path.join(data_dir, filename)
            df = pd.read_csv(path)
            
            if 'title' not in df.columns or 'selftext' not in df.columns:
                print(f"Skipping {filename} (missing columns)")
                continue

            df['text'] = df['title'].fillna('') + ' ' + df['selftext'].fillna('')
            df['clean_text'] = df['text'].apply(clean_text)
            df['tokens'] = df['clean_text'].apply(tokenize)
            dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    full_df = full_df.dropna(subset=['group', 'clean_text'])
    return full_df
