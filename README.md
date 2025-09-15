# Spotify Rock Anthems Dashboard  

A data analysis project exploring the key factors behind the most popular rock songs.  
The dataset is built by collecting data from **Spotify's Web API**, enriched with multiple API integrations and **NLP techniques** for lyrics analysis.

The results are visualized through an interactive **Power BI Dashboard**.

![ProjectSpotifyDashboard](https://github.com/user-attachments/assets/34a49fed-43e9-45c4-875c-fca0add26843)

## Table of Contents  

1. [Project Overview](#project-overview)  
2. [Data Collection](#data-collection)  
3. [Dashboard Sections](#dashboard-sections)
4. [How to Run the Project](#how-to-run-the-project)
5. [Author & Tools](#author--tools)  


## Project Overview

The main objective of this project is to build a comprehensive dataset of rock anthems, starting from Spotify’s official **"Rock Anthems"** playlists for each decade.  
The dataset is enriched with metadata, lyrics, and sentiment analysis, enabling deeper insights into the characteristics of popular rock songs.

<img width="6912" height="2768" alt="PlaylistsBanner" src="https://github.com/user-attachments/assets/272c683d-f38d-4774-9c55-052c357269b1" />


## Data Collection

- **Spotify API**: Used to collect track metadata such as artists, album, release date, duration.
- **Last.fm API**: Added additional information including track descriptions and cover images.
- **Genius API**: Extracted lyrics for each track.
- **MusicBrainz API**: Collected artist-level metadata such as country, gender, band type, and career start date.

## Dashboard Sections  

### 1. Home  

Collects all the features of rock anthems in a single pane, highlighting the key factors that contribute to a successful rock song.
Contents of this section and technical details:

- KPI cards for total songs, average duration, most popular artist, and most popular song, which dynamically update based on user selections and filtering activity.
- Time analysis section with bar and line charts showing average duration, artist categories, and popularity by decade.
- Lyrics analysis with gauge and trend lines, displaying the positive score of lyrics and overall sentiment trends.
- Pie chart showing the percentage of tracks within the selected category. Field parameters are used to group fields in the slicer, and a bookmark is applied to switch between All songs or Top 50 based on user selection.

### 2. Songs

An exploratory page of rock anthems sorted by popularity, displaying detailed information about each track such as duration and years since release.
By clicking on a single song, the lyrics can be accessed, and on hover a summary of song information sourced from Wikipedia is displayed.
Users can filter the view by selecting a playlist or by using the available filters to search for a specific track or generate a customized list.
Contents of this section and technical details:

- Buttons with custom images and bookmarks for filtering by selected playlists.
- Custom columns are used to map specific fields, enabling easier selection for users.
- Table formatting and conditional formatting have been applied to display data bars, URL icons, and song covers.
- A tooltip with a Wikipedia summary is used for the on-hover summary.
- DAX measures are implemented to achieve advanced visualization goals, such as displaying lyrics on click.

### 3. Artists

A section focused on artists, providing demographic and geographic information correlated with their popularity metrics on Spotify.
Contents of this section and technical details:

- A Vertical list filter and between slicer enable user to analyze in deep artists on a custom selection based on decade and age of artist or years since foundation of a band.
- a field parameter tile slicer enable to show the list of artists order by spotify followers, popularity or song popularity.
- KPI cards for Average age and artists category.
- Treemap to show count of artists from UK, USA or other
- Dynamic ArcGIS Map show distribution of artists on the map.
- The magic happens when an artist of the list is selected, it will show all information about the artist, such as, Spotify followers and popularity, Spotify artist image, age and place on the map, this is possible through a series of DAX measures that enable to filter, hide and show information by click.

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
