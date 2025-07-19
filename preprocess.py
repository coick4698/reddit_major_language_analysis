import pandas as pd
import re

subreddit_to_group = {
    'mit': 'STEM',
    'caltech': 'STEM',
    'georgiatech': 'STEM',
    'yale': 'Humanities',
    'columbia': 'Humanities',
    'harvard': 'Humanities',
    'upenn': 'Business',
    'nyu': 'Business',
    'wharton': 'Business'
}

def load_and_preprocess(csv_path):
    df = pd.read_csv(csv_path)
    
    df["subreddit_group"] = df["subreddit.name"].str.lower().map(subreddit_to_group)
    df["text"] = df["title"].fillna('') + ' ' + df["selftext"].fillna('')
    
    def preprocess_text(text):
        text = text.lower()
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'[^a-z\s]', '', text)
        return text.strip()
    
    df['clean_text'] = df['text'].apply(preprocess_text)
    
    df = df.dropna(subset=['clean_text', 'subreddit_group'])
    return df