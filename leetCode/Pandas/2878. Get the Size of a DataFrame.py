from typing import List

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df=pd.DataFrame(players)
    [r,c]=df.shape
    return [r,c]


print(getDataframeSize({'col1': [1, 2], 'col2': [3, 4],
                   'col3': [5, 6]}))