# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\\Users\\hp\\Downloads\\SampleSuperstore.csv')
# print(df)  # to print the table
# print(df.head()) #to print the first five rows
# print(df.Profit) # to print the particular column
# print(df.describe(include='all'))  # to print descriptive statistical data showing all input columns
# print(type(df))
# print(df['Profit'].sort_values())  #sorting only series by default in ascending order
# print(df.sort_values('Profit'))   #Sorting a series along with dataframe
# print(df.sort_values(['Profit', 'Region'])) #Sorting of multiple series
# print(df.shape)   # Total number of rows and columns
# print(df.drop(4, axis=0).head())  #droping a row
# print(df.mean())  # calculating mean of a particular series
# print(df.mean(axis=1))   d # calculating mean of a particular row
# print(sns.relplot('Sales','Profit',data=df))  ##shows the min and max profit of the sales
# plt.show()
print(sns.countplot('Ship Mode', data=df))  ## shows which ship mode is used the most
plt.show()
# print(sns.relplot('Sales', 'Profit', data=df, col='Segment'))  # shows different analysis for each segment
# plt.show()
# print(df.select_dtypes(include=[np.number]).columns)  # showing which fields are of numeric data
# plt.show()
# ship_mode=df.groupby('Ship Mode')['Profit', 'Quantity'].sum() # showing which ship mode is having highest profit
# print(ship_mode)
# Region=df.groupby('Region')['Profit', 'Quantity'].sum()
# print(Region)
# Now we are finding which region has the highest profits
# plt.bar('Region', 'Total profits', align='center', alpha=0.5, color="#008fd5")  # shows total profit regionwise
# plt.ylabel('Total Profits')
# plt.title('Profit in Regions')
# plt.legend()
# plt.show()
# plt.figure(figsize=(7,7))
# sns.lineplot(x='Discount', y='Profit', data=df, color='b')  #shows discounts are higher, not converted into profits
# plt.show()
# sns.boxplot(x='Profit', y='Ship Mode', data=df)
# plt.show()
# City=df.groupby('City')['Profit', 'Quantity'].sum()   # showing the profit and corresponding quantity citywise
# print(City)

