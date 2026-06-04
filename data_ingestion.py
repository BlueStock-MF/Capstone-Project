import pandas as pd
import os

data_folder = "data/raw"

for file in os.listdir(data_folder):

    if file.endswith(".csv"):

        path = os.path.join(data_folder, file)

        df = pd.read_csv(path)

        print("\n" + "="*50)
        print(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print(df.isnull().sum())

        print(df.duplicated().sum())