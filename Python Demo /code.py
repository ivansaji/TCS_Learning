import pandas as pd
ls=[]

data=pd.read_excel(r'./data.xlsx')
val=input("Enter the date")
df=pd.DataFrame(data, columns=[val])
print(df)