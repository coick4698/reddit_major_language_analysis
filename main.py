from preprocess import load_and_preprocess_all
from collections import Counter

"""
- analyzing function
- extract and list the top N most frequent words for each group
"""
def compare_focus_words(group_word_counts, top_n=100):
    focus_words = {}
    all_groups = list(group_word_counts.keys())

    for group in all_groups:
        other_groups = [g for g in all_groups if g != group]
        group_top = set([word for word, _ in group_word_counts[group].most_common(top_n)])
        others_top = set()
        for g in other_groups:
            others_top.update([word for word, _ in group_word_counts[g].most_common(top_n)])
        
        unique = group_top - others_top
        focus_words[group] = unique

    return focus_words

print(" Loading and preprocessing data...")
df = load_and_preprocess_all()

# count word by group
print("\n Calculating word frequencies...")
group_word_counts = {}
for group in df['group'].unique():
    tokens = df[df['group'] == group]['tokens'].explode()
    counter = Counter(tokens)
    group_word_counts[group] = counter

    print(f"\n Top words in {group}:")
    for word, count in counter.most_common(10):
        print(f"{word}: {count}")

print("\n Comparing group-specific vocabulary...")
focus = compare_focus_words(group_word_counts, top_n=100)

for group, words in focus.items():
    print(f"\n Unique words in {group}:")
    print(', '.join(list(words)[:15]))
