import glob
import pandas as pd

path = r'C:\Users\vishn\OneDrive\Desktop\aws2'
csv_files = glob.glob(path + "/*.csv")
n = len(csv_files)
# li = csv_files[n - 1:n - 1 - 24:-1]
# li2 = csv_files[n - 24:n - 1 - 48:-1]
# li3 = csv_files[n - 48:n - 1 - 72:-1]
li = csv_files[n - 1:n - 1 - 144:-1]
# print(li)

df_list = (pd.read_csv(file,
                       sep=';',
                       engine='python') for file in li)

big_df = pd.concat(df_list, ignore_index=True)
big_df = big_df.iloc[1:, :]
big_df['date'] = pd.to_datetime(big_df['date'], dayfirst=True, errors='coerce', utc=True)
df2 = pd.read_csv("final_aws.csv")
df_grouped = pd.merge(big_df, df2)
df_grouped = df_grouped[["#id", "date"]]
df_grouped = df_grouped.drop_duplicates()
df_grouped['date'] = df_grouped['date'].dt.tz_convert('Asia/Kolkata')
df_grp = (df_grouped.groupby(['date']))['#id'].count().rename('No. of Stations').to_frame()
dfa = df_grp.reset_index()
