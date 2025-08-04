import pandas as pd

# delete intro in lyrics - a short string added from the API
def clean_lyrics_intro(text):
    if pd.isna(text):
        return ""
    
    if '… Read More' in text:
        text = text.split('… Read More')[-1]
    elif 'Lyrics' in text:
        text = text.split('Lyrics')[-1]
    
    return text.strip()

# load dataset
df = pd.read_csv("insert_your_path/RockAnthemsDataset_PowerBI_dataset.csv")

# clean lyrics
df['lyrics'] = df['lyrics'].apply(clean_lyrics_intro)

# save dataset
output_path = "insert_your_path/RockAnthemsDataset_PowerBI_dataset_lyricsCleaned.csv"
df.to_csv(output_path, index=False)

print("Lyrics cleaned and saved in:\n", output_path)
