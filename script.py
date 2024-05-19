# import pandas as pd
# df1 = pd.read_csv('output.txt')
# df1=set(df1)
# print((df1))
import time
print("Start Time",time.time())

a = open('output.txt', 'r').readlines()
b = open('total details.txt', 'r').readlines()
print("End Time",time.time())

output = []

for item in b:
    if item not in a:
        output.append(item)

with open('resultant.txt', 'w') as res:
    for line in output:
        res.write(line)

print("End Time after process",time.time())