import os
import glob
import pandas as pd

path = r"C:\Users\vishn\OneDrive\Desktop\7 days file"
csv_files = glob.glob(path + "/*.csv")


with open(r"C:\Users\vishn\OneDrive\Desktop\dashboards\total_stations.txt") as f:
    var = [int(i) for i in f.readline().split()]

s = [str(integer) for integer in var]
a_string = "".join(s)

t = int(a_string)
# print(t)
j = 0
df = {}

for i in csv_files:
    with open(i, 'r', encoding="latin-1") as csvfile:
        x = os.path.basename(i)
        x = x[0:10]
        y = str(len(csvfile.readlines()) - 1)
        y = int(y)
        # z=(y/t)*100
        # k=round(z,1)
        # data1= [x,t]
        # data.append(data1)
        n = t - y
        df[j] = pd.DataFrame([[x, y]], columns=['date', 'No. of Stations'])
        dfa = {'date': 'Missing', 'No. of Stations': n}
        df[j] = df[j].append(dfa, ignore_index=True)
        j = j + 1

# print(df[0])
# print(df[1])
# print(df[2])
# print(t)
#print(df)