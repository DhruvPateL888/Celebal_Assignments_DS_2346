#Username : CT_CSI_DS_2346
#Name : Dhruv Patel

# Imprting the Libraries
import pandas as pd
import numpy as np
from sklearn import preprocessing
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
sns.set_style('whitegrid')

# Loading the Dataset
df = pd.read_csv('Placement_Data_Full_Class.csv')

#Viewing Dataset
df.head(10)
df.info()

#Data Preprocessing
df.drop('sl_no', inplace = True, axis = 1)
df.isnull().sum()

#Dataset after Preprocessing
df.describe()

#Placement Statistics
placed_members = len(df[df['status'] == "Placed"])
unplaced_members = len(df[df['status'] == 'Not Placed'])
x = np.zeros(2)
x[0] = placed_members
x[1] = unplaced_members
print("Placed_members Count : ",placed_members )
print("Unplaced_members Count : ",unplaced_members )
plt.title('Placement Status')
plt.pie(x, labels = ['no_placed_members', 'no_unplaced_members'],shadow =True)
plt.show()

#Gender Destribution

male_count = len(df[df['gender'] == 'M'])
female_count = len(df[df['gender'] == 'F'])
x = np.zeros(2)
x[0] = male_count
x[1] = female_count
print("Male Count : ",male_count )
print("Female Count : ",female_count )
plt.title('Gender Distribution')
plt.pie(x, labels = ['Male', 'Female'],shadow =True)
plt.show()




