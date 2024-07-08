import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(products)
    df[['quantity']] = df[['quantity']].fillna(0)
    return df

data = {'name':['Wristwatch','WirelessEarbuds','GolfClubs','Printer'],'quantity':[None,None,3,4],'price':[None
    ,821,9319,3051]}

print(fillMissingValues(data))