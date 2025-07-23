import musicbrainzngs
import pandas as pd
import time


musicbrainzngs.set_useragent("YourApp", "1.0", "your@email.com")

df = pd.read_csv("insert_your_path/RockAnthemsDataset_enriched_lyrics.csv")

# distinct artists from dataset
unique_artists = df['artists'].unique()

# collect artist details here
artist_data = []

def get_artist_info(artist_name):
    try:
        result = musicbrainzngs.search_artists(query=artist_name, limit=1)
        if result['artist-list']:
            artist = result['artist-list'][0]
            return {
                "artist": artist_name,
                "country": artist.get('country', 'Unknown'),
                "area": artist.get('area', {}).get('name', 'Unknown'),
                "begin_area": artist.get('begin-area', {}).get('name', 'Unknown'),
                "type": artist.get('type', 'Unknown'),
                "gender": artist.get('gender', 'Unknown'),
                "begin_date": artist.get('life-span', {}).get('begin', 'Unknown'),
            }
    except Exception as e:
        print(f"Error for {artist_name}: {e}")
    return {
        "artist": artist_name,
        "country": "Unknown",
        "area": "Unknown",
        "begin_area": "Unknown",
        "type": "Unknown",
        "gender": "Unknown",
        "begin_date": "Unknown",
    }


for i, artist in enumerate(unique_artists):
    print(f"{i+1}/{len(unique_artists)} → {artist}")
    artist_info = get_artist_info(artist)
    artist_data.append(artist_info)
    time.sleep(1)  # to don't exceed MusicBrainz limit

# Save in CSV
artist_df = pd.DataFrame(artist_data)
artist_df.to_csv("insert_your_path/RockAnthemsDataset_artist_info.csv", index=False)

print("Well done!")
