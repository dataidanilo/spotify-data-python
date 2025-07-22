import pandas as pd
import pylast
import time

# Last.fm API credentials
API_KEY = "insert_your_api_key"
API_SECRET = "insert_your_api_secret"
username = "insert_your_username"
password_hash = pylast.md5("insert_your_password")

# connect to Last.fm
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=username, password_hash=password_hash)

# load cleaned dataset
df = pd.read_csv('insert_your_path/RockAnthemsDataset_cleaned.csv')

# new columns
df['lastfm_summary'] = None
df['lastfm_cover_image'] = None

# ingest new data for each row
for idx, row in df.iterrows():
    artist = row['artists'].split(',')[0]  # only the first artist
    track_name = row['track_name']
    
    try:
        track = pylast.Track(artist, track_name, network)
        summary = track.get_wiki_summary()
        cover_image = track.get_cover_image()
    except Exception as e:
        summary = None
        cover_image = None
        print(f"Error for {artist} - {track_name}: {e}")

    df.at[idx, 'lastfm_summary'] = summary
    df.at[idx, 'lastfm_cover_image'] = cover_image

    time.sleep(0.3)  

# save enriched csv
df.to_csv('insert_your_path/RockAnthemsDataset_enriched.csv', index=False)
print("dataset saved")