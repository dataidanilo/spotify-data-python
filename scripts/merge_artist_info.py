import pandas as pd

# load datasets
tracks_df = pd.read_csv("insert_your_path/RockAnthemsDataset_enriched_lyrics.csv")
artists_df = pd.read_csv("insert_your_path/RockAnthemsDataset_artist_info.csv")

# merge and drop duplicated column
merged_df = tracks_df.merge(artists_df, how='left', left_on='artists', right_on='artist')
merged_df.drop(columns=['artist'], inplace=True)

# save dataset
merged_df.to_csv("insert_your_path/RockAnthemsDataset_PowerBI_dataset.csv", index=False)

print("Merge completed!")
