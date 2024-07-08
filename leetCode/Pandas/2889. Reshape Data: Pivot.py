import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(weather).pivot(index='month', columns='city', values='temperature')
    return df

data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'month': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan',
              'Feb', 'Feb', 'Feb', 'Feb', 'Feb',
              'Mar', 'Mar', 'Mar', 'Mar', 'Mar'],
    'temperature': [30, 50, 20, 60, 55,
                    32, 55, 25, 65, 60,
                    40, 60, 30, 70, 65]
}

print(pivotTable(data))