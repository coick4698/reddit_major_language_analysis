# token by clean_text
# count word_frequency by group
# get top 100 words

from collections import Counter
from preprocess import load_and_preprocess
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def tokenize(text):
    words =  text.split()
    return [word for word in words if word not in stop_words and len(word) > 8]


def get_word_frequencies_by_group(df):
    group_freq = {}
    
    for group in df['subreddit_group'].unique():
        texts = df[df['subreddit_group'] == group]['clean_text']
        tokens = []
        for text in texts:
            tokens.extend(tokenize(text))
        group_freq[group] = Counter(tokens)

    return group_freq

if __name__ == "__main__":
    df = load_and_preprocess("dataset/posts_samples.csv")
    freqs = get_word_frequencies_by_group(df)
    
    for group, counter in freqs.items():
        print(f"🔹 {group} Top words:")
        print(counter.most_common(10))
        print()