import os
import glob
import pandas as pd

path = r"C:\Users\vishn\OneDrive\Desktop\7 days file"
csv_files = glob.glob(path + "/*.csv")
data = []

for i in csv_files:
    with open(i, 'r', encoding="latin-1") as csvfile:
        x = os.path.basename(i)
        x = x[0:10]
        y = str(len(csvfile.readlines()) - 1)
        data1 = [x, y]
        data.append(data1)

dfd = pd.DataFrame(data, columns=['date', 'No. of Stations'])
# print(dfd)
