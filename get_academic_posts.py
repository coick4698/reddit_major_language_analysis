import praw
import pandas as pd
import time
import os

# personal information
CLIENT_ID = '22UOcw1-QDM1j0JZ1RIn_g'
CLIENT_SECRET = '6rehjaMDbL9ksAuteJi9Q12kfjfljQ'
USER_AGENT = 'reddit-major-language-analysis-script'

# connect Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# opt subreddit
subreddits = {
    'STEM': 'computerscience',
    'Humanities': 'AskPhilosophy',
    'Business': 'MBA'
}

# collect posts
def fetch_posts(subreddit_name, limit=300):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for submission in subreddit.hot(limit=limit):
        posts.append({
            'id': submission.id,
            'title': submission.title,
            'selftext': submission.selftext,
            'created_utc': submission.created_utc,
            'subreddit': subreddit_name
        })
    return pd.DataFrame(posts)

# fetch data(AI used)
def fetch_all(save_dir='data'):
    os.makedirs(save_dir, exist_ok=True)
    for group, subreddit in subreddits.items():
        print(f' Fetching from r/{subreddit} ...')
        df = fetch_posts(subreddit, limit=300)
        df['group'] = group
        save_path = os.path.join(save_dir, f'{group.lower()}_posts.csv')
        df.to_csv(save_path, index=False)
        print(f' Saved {len(df)} posts to {save_path}')
        time.sleep(2)

if __name__ == '__main__':
    fetch_all()
