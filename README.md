# Reddit Major Language Analysis

This project analyses vocabulary usage differences across academic fields using Reddit.
By examining subreddit data from STEM, Humanities, and Business communities, we aim to uncover sociopsychological patterns in vocabulary and communication styles.

---

## Project Overview

- **Goal**: Identify and compare frequently used words across different academic groups.
- **Data Source**: Reddit posts from three subreddits:
  - `r/computerscience` (STEM)
  - `r/AskPhilosophy` (Humanities)
  - `r/MBA` (Business)
- **Method**:
  1. Crawled 300 posts from each subreddit using PRAW (Reddit API).
  2. Preprocessed text data: lowercasing, tokenization, stopword removal, and special character filtering.
  3. Counted word frequencies and extracted top words per group.
  4. Visualized results using WordClouds and Bar Charts.

---

## File Structure
reddit_major_language_analysis/
│
├── get_academic_posts.py
├── preprocess.py
├── main.py
├── word_analysis.ipynb
│
├── data/
└── README.md

---

## Results(Visualising)

### Bar Charts

*(Top 10 most frequent words in 3 different groups)*

---

### Key Findings

- Each academic group shows unique word usage patterns.
- STEM posts tend to be technical and code-oriented.
- Humanities discussions include more abstract, philosophical vocabulary.
- Business posts focus on practical topics such as strategy, career, and MBA.

---

### Requirements (external libraries)

- praw
- pandas
- matplotlib
- seaborn
- nltk
- re
- os
- collections
- time

---

## Author

- **Doyeop Kim**
  BSc in Computer Science, University of Exeter
  GitHub: [coick4698/reddit_major_language_analysis]
  Date: July 2025

---

## License

This project is open-source and free to use for educational purposes.
