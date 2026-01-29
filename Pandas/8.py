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
exc= pd.read_excel("Pandas/adult.xlsx")
# print(exc.head(5))

df = pd.read_csv("Pandas/titanic.csv")
# print(df.head())

# df.info()

# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df.to_csv("titanic_filled.csv")
# fdf = pd.read_csv("titanic_filled.csv")
# print(f"Number of null values in Age column in filled CSV: {fdf['Age'].isnull().sum()}")
# print(f"Number of null values in Age column in original CSV: {df['Age'].isnull().sum()}")

# df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# df.drop(columns=['Cabin'], inplace=True)

# print(df['Embarked'].isnull().sum())

# df.rename(columns={'Sex':'Gender'}, inplace=True)  



# df['Gender'] = df['Gender'].replace('male', 'M')

# print(df['Gender'])



sealions = pd.DataFrame({
    "id": [10484,11728,11729,11732,11734,11790],
    "name": ['Ayah','Spot','Tiger','Mabel','Rick','Jolee']
})

migrations = pd.DataFrame({
    "id": [10484,11728,11729,11732,11734,11735,11736,11737],
    "distance": [1000,1531,1370,1622,1491,2723,1571,1957],
    "days": [107,56,37,62,58,82,52,92]
})

# print(sealions)
# print(migrations)

print("\n Inner join\n", sealions.merge(migrations, on="id", how="inner"))
print("\nLeft join\n", sealions.merge(migrations, on="id", how="left"))
print("\n Right join\n", sealions.merge(migrations, on="id", how="right"))
print("\n Outer join\n", sealions.merge(migrations, on="id", how="outer"))