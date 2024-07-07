from typing import List

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    result = pd.DataFrame(student_data,columns=['student_id','age'] )
    return result
createDataframe([
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
])