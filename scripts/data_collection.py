import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API Credentials
# Generated on https://developer.spotify.com/

CLIENT_ID = "insert_yours_here"
CLIENT_SECRET = "insert_yours_here"

# Spotipy authentication
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


# Rock playlists chosen for this project
playlist_ids = [
    "57ChLERiMe1xIpKrN2yK58",
    "5D9BB7GAk7CgFSBMm56DFw",
    "3zbfl6fl2qOPDzLHXtYokd",
    "2uqwvVc4Y2FMlslXJGLiz4",
    "2FrdP2LsR751HGkcyEzwK2",
    "1M63Hi4J1oTXgpqCUBfjV2"
]



# ID extraction from playlist URL
# If there is an optional parameter (?) in the URL, it will be managed
def extract_playlist_id(url):
    return url.split("/")[-1].split("?")[0] 

# data extraction
tracks_data = []

for playlist_id in playlist_ids:
    playlist = sp.playlist(playlist_id)
    playlist_name = playlist["name"]
    print(f"Data extracted from the playlist: {playlist_name}")

    results = sp.playlist_items(playlist_id, additional_types=['track'])

    for item in results['items']:
        track = item['track']
        if track is None:
            continue

        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album = track['album']['name']
        release_date = track['album']['release_date']
        duration_ms = track['duration_ms']
        popularity = track['popularity']
        track_url = track['external_urls']['spotify']

        tracks_data.append({
            'playlist': playlist_name,
            'track_name': track_name,
            'artists': artists,
            'album': album,
            'release_date': release_date,
            'duration_ms': duration_ms,
            'popularity': popularity,
            'url': track_url
        })


# save data in CSV
df = pd.DataFrame(tracks_data)
print(df.head())

df.to_csv('Insert_your_path_here/RockAnthemsDataset.csv', index=False)