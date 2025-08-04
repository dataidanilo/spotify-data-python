import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nrclex import NRCLex
import string

nltk.download('stopwords')
nltk.download('vader_lexicon')

# load dataset
df = pd.read_csv("insert_your_path/RockAnthemsDataset_PowerBI_dataset_lyricsCleaned.csv")

# text cleaning function
def clean_lyrics(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)  # remove songs sections, such as [chorus]
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # link
    text = re.sub(f"[{re.escape(string.punctuation)}]", '', text)  # punctuation
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')] # remove stopwords
    return " ".join(tokens)

# clean lyrics in dataset
df['clean_lyrics'] = df['lyrics'].apply(clean_lyrics)

# sentiment analysis
sia = SentimentIntensityAnalyzer()

df['sentiment_score'] = df['clean_lyrics'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment_label'] = df['sentiment_score'].apply(
    lambda x: 'positive' if x > 0.2 else ('negative' if x < -0.2 else 'neutral')
)

# emotions analysis
def extract_emotions(text):
    if not text:
        return {}
    emotion = NRCLex(text)
    emotions_count = emotion.raw_emotion_scores
    return emotions_count

# add emotions columns
emotion_data = df['clean_lyrics'].apply(extract_emotions)
emotion_df = pd.json_normalize(emotion_data)

# 0 instead null
emotion_df = emotion_df.fillna(0).astype(int)

# new dataset
final_df = pd.concat([df, emotion_df], axis=1)

# save csv
final_df.to_csv("insert_your_path/RockAnthemsDataset_PowerBI_dataset_withNLP.csv", index=False)
print("Dataset enriched with lyrics analysis, well done!")
