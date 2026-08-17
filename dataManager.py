from io import BytesIO

import requests
import pandas as pd

def getGoogleSheet():
    r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1zNKPjLWWRia4eNqX5SIUx67sBXv8y_Bq0d3YU8zxeO8&output=csv')
    data = r.content

    df = pd.read_csv(BytesIO(data))
    df = df[["Date", "Total Balance", "Cash Balance", "Account Balance", "Amount", "Payment Method", "Shop/Person", "Location", "Description", "Category"]]
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%Y")
    df = df.sort_values("Date")
    return df;

def mine():
    df = getGoogleSheet()
    print(df.to_string())
    print(df.dtypes)