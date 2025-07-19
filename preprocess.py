import pandas as pd
import os
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# ✅ 텍스트 클렌징 함수
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # URL 제거
    text = re.sub(r"[^a-z\s]", "", text)  # 특수문자 제거
    return text

# ✅ 토큰화 함수
def tokenize(text):
    tokens = text.split()
    return [t for t in tokens if t not in stop_words and len(t) > 1]

# ✅ 전처리 전체 로딩
def load_and_preprocess_all(data_dir="data"):
    dfs = []
    for filename in os.listdir(data_dir):
        if filename.endswith("_posts.csv"):
            path = os.path.join(data_dir, filename)
            df = pd.read_csv(path)

            if 'title' not in df.columns or 'selftext' not in df.columns:
                print(f"⚠️ Skipping {filename} (missing columns)")
                continue

            df['text'] = df['title'].fillna('') + ' ' + df['selftext'].fillna('')
            df['clean_text'] = df['text'].apply(clean_text)
            df['tokens'] = df['clean_text'].apply(tokenize)
            dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    full_df = full_df.dropna(subset=['group', 'clean_text'])
    return full_df
