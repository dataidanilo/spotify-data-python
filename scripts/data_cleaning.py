import pandas as pd

# load dataset
df = pd.read_csv('Insert_your_path_here/RockAnthemsDataset.csv')

# each selected playlist name has " (2)" at the end, which is not useful
df['playlist'] = df['playlist'].str[:-4]

# clean track names
df['track_name'] = df['track_name'].str.split(' - ').str[0]

# duration in sec
df['duration_sec'] = (df['duration_ms'] / 1000).astype(int)
df = df.drop(columns=['duration_ms'])

# check
print(df.head())

# save cleaned dataset
df.to_csv('Insert_your_path_here/RockAnthemsDataset_cleaned.csv', index=False)
