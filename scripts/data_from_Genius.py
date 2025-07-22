import pandas as pd
import lyricsgenius
import time

# genius API authentication
genius = lyricsgenius.Genius("insert_your_token")
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]
genius.remove_section_headers = True

# load data
df = pd.read_csv('insert_your_path/RockAnthemsDataset_enriched.csv')

# add lyrics column
df['lyrics'] = None

# iterate for each row
for idx, row in df.iterrows():
    artist = row['artists'].split(',')[0]  # only the first artist
    track_name = row['track_name']
    
    try:
        song = genius.search_song(track_name, artist)
        lyrics = song.lyrics if song else None
    except Exception as e:
        lyrics = None
        print(f"Error for {artist} - {track_name}: {e}")

    df.at[idx, 'lyrics'] = lyrics
    print(f"{artist} - {track_name} loaded")
    
    time.sleep(1.5)  # to don't exceed the rate limit

# save 
df.to_csv('insert_your_path/RockAnthemsDataset_enriched_lyrics.csv', index=False)
print("dataset saved")
