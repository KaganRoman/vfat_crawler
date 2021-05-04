import os
import pandas as pd

from constants import BLOCKCHAIN_LIST

def list_of_csvs():
    folder = "./results/"
    csvs = os.listdir(folder)
    csvs.sort(reverse=True)
    latest_csvs = {k:None for k in BLOCKCHAIN_LIST}
    for csv in csvs:
        not_found_bc = [k for (k,v) in latest_csvs.items() if not v]
        if not not_found_bc:
            break
        for bc in not_found_bc:
            if csv.endswith(f'{bc}.csv'):
                latest_csvs[bc] = folder + csv
    return list(latest_csvs.values())


def load_pd(csvs):
    li = []
    for filename in csvs:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    df = pd.concat(li, axis=0, ignore_index=True)
    df['Staked'] = df['Staked'].str.replace(',', '').astype(float)
    return df


if __name__ == '__main__':
    csvs = list_of_csvs()
    print(csvs)
    df = load_pd(csvs)
    print(df.dtypes)
    df = df.sort_values(by="Staked", ascending=False)    
    print(df.head(50))
