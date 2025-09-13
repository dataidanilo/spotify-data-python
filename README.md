# Spotify Rock Anthems Dashboard  

A data analysis project exploring the key factors behind the most popular rock songs.  
The dataset is built by collecting data from **Spotify's Web API**, enriched with multiple API integrations and **NLP techniques** for lyrics analysis.

The results are visualized through an interactive **Power BI Dashboard**.

![ProjectSpotifyDashboard](https://github.com/user-attachments/assets/34a49fed-43e9-45c4-875c-fca0add26843)

## Table of Contents  

1. [Project Overview](#project-overview)  
2. [Data Collection](#data-collection)  
3. [How to Run the Project](#how-to-run-the-project)
4. [Author & Tools](#author--tools)  


## Project Overview

The main objective of this project is to build a comprehensive dataset of rock anthems, starting from Spotify’s official **"Rock Anthems"** playlists for each decade.  
The dataset is enriched with metadata, lyrics, and sentiment analysis, enabling deeper insights into the characteristics of popular rock songs.

<img width="6912" height="2768" alt="PlaylistsBanner" src="https://github.com/user-attachments/assets/272c683d-f38d-4774-9c55-052c357269b1" />


## Data Collection

- **Spotify API**: Used to collect track metadata such as artists, album, release date, duration.
- **Last.fm API**: Added additional information including track descriptions and cover images.
- **Genius API**: Extracted lyrics for each track.
- **MusicBrainz API**: Collected artist-level metadata such as country, gender, band type, and career start date.

## How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SpotifyProject.git
   cd SpotifyProject
   ```
2. Create and activate a virtual environment:  
   ```bash
   # Choose the path (project folder is recommended)
   cd yourpath

   # Create the venv
   python -m venv .venv  

   # Activate the venv  
   # On Windows
   .venv\Scripts\activate  

   # On macOS/Linux
   source .venv/bin/activate  
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the project:
    - Open scripts/data_collection.py and replace the playlist IDs with the ones you want to analyze.
    - Update file paths inside the scripts if needed.
    - Add your API keys.
4. Run scripts step by step from the `scripts/` folder in the following order:
    ```bash
    python scripts/data_collection.py          # Collect data from Spotify playlists
    python scripts/data_cleaning.py            # Clean raw data
    python scripts/data_from_LastFM.py         # Fetch additional artist info from LastFM
    python scripts/data_from_Genius.py         # Get lyrics from Genius
    python scripts/data_from_musicbrainz.py    # Enrich with MusicBrainz metadata
    python scripts/merge_artist_info.py        # Merge artist metadata
    python scripts/clean_intro_lyrics.py       # Clean intro lines from lyrics
    python scripts/lyrics_nlp_analysis.py      # Perform sentiment analysis on lyrics
   ```


## Author & Tools

**Author**: Danilo Cassatella  

**Tools & APIs**:  
- **Music & Data**: Spotify, Last.fm, Genius, MusicBrainz  
- **Data Analysis & NLP**: Pandas, NLTK, NRCLex  
- **Visualization**: Power BI  

**Contact**:  
- Email: danilocassatella@gmail.com  
- LinkedIn: [linkedin.com/in/danilocassatella](https://www.linkedin.com/in/danilocassatella/)
