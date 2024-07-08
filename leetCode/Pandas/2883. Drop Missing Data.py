import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    df=df[df['name'].notna()]
    return df


data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    'name': [
        'John', 'Jane', 'Doe', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank',
        'Grace', 'Hank', 'Ivy', 'Jack', 'Kelly', 'Liam', 'Mona', 'Nina', 'Oscar',
        'Paul', 'Quincy', 'Rachel', 'Sam', 'Tom', 'Uma', 'Vince'
    ],
    'email': [
        'john@example.com', 'jane@example.com', 'doe@example.com', 'alice@example.com', 'bob@example.com',
        'charlie@example.com', 'david@example.com', 'eve@example.com', 'frank@example.com',
        'grace@example.com', 'hank@example.com', 'ivy@example.com', 'jack@example.com', 'kelly@example.com',
        'liam@example.com', 'mona@example.com', 'nina@example.com', 'oscar@example.com', 'paul@example.com',
        'quincy@example.com', 'rachel@example.com', 'sam@example.com', 'tom@example.com', 'uma@example.com',
        'vince@example.com'
    ],
    'salary': [
        50000, 60000, 55000, 70000, 65000, 72000, 48000, 53000, 76000, 54000,
        58000, 69000, 62000, 51000, 63000, 74000, 56000, 52000, 68000, 59000,
        67000, 75000, 61000, 64000, 57000
    ],
    'age': [
        28, 34, 45, 25, 30, 32, 41, 29, 33, 38,
        36, 40, 31, 27, 35, 43, 39, 26, 37, 42,
        44, 24, 46, 50, 47
    ]
}
print(dropMissingData(data))
