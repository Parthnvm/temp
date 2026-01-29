#Pandas

import pandas as pd

s1 = pd.Series([10,20,30,40,50,60,70,80,90,100])
# print(s1)

# print(s1.head()) # .head shows the 1st 5 rows by default
# print(s1.head(1)) # shows the 1st row only

# df = pd.DataFrame(
#     {
#         "id": [1,2,3,4,5],
#         "name": ["Parth","Atharva","Sumit","Rohit","Ankit"],
#         "age": [20,21,22,23,24]
#     }
    
# )



# df.info()


# print(df[['name','age']])

df = pd.read_csv("Pandas/temp.csv")
print(df.head())