import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

print(data.head())
print(data.tail())
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())
median_age = data['Age'].median()
data['Age'].fillna(median_age, inplace=True)
mode_embarked = data ['Embarked'].mode()[0]
data['Embarked'].fillna(mode_embarked, inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data['FamilySize'] = data['SibSp'] + data['Parch']