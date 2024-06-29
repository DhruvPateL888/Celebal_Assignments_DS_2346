#Username : CT_CSI_DS_2346
#Name : Dhruv Patel

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


#importing the dataset

df = pd.read_csv('Black Friday Dataset.csv')
df.head()


#Information and Basic Description of dataset
df.info()
df.describe()

#As user id will not be usefull for the prediction
df.drop(['User_ID'],axis=1,inplace=True)

df.head()


#Handling categorical feature Gender
df['Gender']=pd.get_dummies(df['Gender'],drop_first=1)
df['Gender']=df['Gender'].map({'F':0,'M':1})
df.head()


# Handle categorical feature Age
df['Age'].unique()


#pd.get_dummies(df['Age'],drop_first=True)
df['Age']=df['Age'].map({'0-17':1,'18-25':2,'26-40':3,'41-50':4,'51-60':5,'60+':6})


##second technqiue
from sklearn import preprocessing
 
# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()
 
# Encode labels in column 'species'.
df['Age']= label_encoder.fit_transform(df['Age'])
 
df['Age'].unique()


df.head()



#fixing categorical City_category

df_city=pd.get_dummies(df['City_Category'],drop_first=True)


df_city.head()

df=pd.concat([df,df_city],axis=1)
df.head()


#drop City Category Feature
df.drop('City_Category',axis=1,inplace=True)


df.head()


# Missing Values
df.isnull().sum()


## Focus on replacing missing values
df['Product_Category_2'].unique()

df['Product_Category_2'].value_counts()


df['Product_Category_2'].mode()[0]


## Replace the missing values with mode
df['Product_Category_2']=df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])

df['Product_Category_2'].isnull().sum()


# Product_category 3 replace missing values
df['Product_Category_3'].unique()


df['Product_Category_3'].value_counts()


# Replace the missing values with mode
df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])


df.head()

df.shape()


df['Stay_In_Current_City_Years'].unique()


df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].str.replace('+','')


df.head()


df.info()


##convert object into integers
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)
df.info()


df['B']=df['B'].astype(int)
df['C']=df['C'].astype(int)

df.info()


# Purchasing of men is high then women

df.head()


##Feature Scaling 
df_test=df[df['Purchase'].isnull()]


df_train=df[~df['Purchase'].isnull()]



X=df_train.drop('Purchase',axis=1)

X.head()
X.shape



y=df_train['Purchase']
y.shape



y


