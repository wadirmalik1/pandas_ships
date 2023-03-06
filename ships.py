import pandas as pd

ships = pd.read_csv(r"C:\Users\WadirMalik\Downloads\ship.csv")

print(ships.count())
print(ships.dtypes)

print(ships.describe())

print(ships.isnull().values.any())

print(sum(pd.isnull(ships['Age'])))
avg_age = ships['Age'].mean()
ships['Age'].fillna(avg_age, inplace=True)

ships.drop(['SibSp'], axis=1, inplace=True)

print(ships.groupby('Gender')['PassengerId'].count())

ships['title'] = ships['Name'].apply(lambda x : x.split('.')[0].split(',')[1].strip())



