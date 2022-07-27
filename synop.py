import glob
import pandas as pd

path = r'C:\Users\vishn\OneDrive\Desktop\synop2'
csv_files = glob.glob(path + "/*.csv")
n = len(csv_files)
# print(n)
# li = csv_files[n - 1:n - 1 - 24:-1]
# li2 = csv_files[n - 24:n - 1 - 48:-1]
# li3 = csv_files[n - 48:n - 1 - 72:-1]
# li4 = csv_files[n - 72:n - 1 - 96:-1]
# li5 = csv_files[n - 96:n - 1 - 120:-1]
# li6 = csv_files[n - 120:n - 1 - 144:-1]
li = csv_files[n - 1:n - 1 - 144:-1]
# print(li)
df_list = (pd.read_csv(file,
                       sep=';',
                       engine='python') for file in li)
big_df = pd.concat(df_list, ignore_index=True)
big_df = big_df.iloc[1:, :]
big_df['date'] = pd.to_datetime(big_df['date'], dayfirst=True, errors='coerce', utc=True)
big_df = big_df[big_df['#id'].str.startswith('42') | big_df['#id'].str.startswith('43')]
big_df['date'] = big_df['date'].dt.tz_convert('Asia/Kolkata')
df = big_df.drop_duplicates()
df_grouped = (df.groupby(['date']))['#id'].count().rename('No. of Stations').to_frame()
dfs = df_grouped.reset_index()
# print(df6)
