import openpyxl
import pandas as pd

new=[]
while True:
    new.append(input("Enter new prize: "))
    r=input("Continue? y/n")
    if r=='n' or r=='N':
        break
    else:
        continue

d = pd.DataFrame(new)
d.to_excel('woftest.xlsx', sheet_name='Sheet1',index=False, header=False)
print(d)