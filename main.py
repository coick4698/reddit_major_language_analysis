from preprocess import load_and_preprocess

df = load_and_preprocess("dataset/posts_samples.csv")
print(df[['subreddit.name', 'subreddit_group', 'clean_text']].head())