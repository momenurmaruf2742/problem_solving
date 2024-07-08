import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students)
    df.columns=['student_id','first_name','last_name','age_in_years']
    return df

data = {
    'id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'first': [
        'John', 'Jane', 'Robert', 'Alice', 'Michael', 'Sarah', 'David', 'Emma', 'Daniel', 'Olivia',
        'James', 'Sophia', 'William', 'Isabella', 'Joseph'
    ],
    'last': [
        'Smith', 'Doe', 'Johnson', 'Brown', 'Williams', 'Jones', 'Garcia', 'Miller', 'Davis', 'Martinez',
        'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White'
    ],
    'age': [28, 34, 45, 25, 30, 32, 41, 29, 33, 38, 36, 40, 31, 27, 35]
}

print(renameColumns(data))