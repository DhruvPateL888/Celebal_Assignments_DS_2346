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

#Working with outliers:

def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False

def grab_col_names(dataframe, cat_th=10, car_th=20):

    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O" and col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

def grab_outliers(dataframe, col_name, outlier_index=False, f = 5):
    low, up = outlier_thresholds(dataframe, col_name)

    if dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].shape[0] > 10:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].head(f))
    else:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))])

    if outlier_index:
        out_index = dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].index
        return out_index

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit



cat_cols, num_cols, cat_but_car = grab_col_names(df)

#Let's see which column has outliers...
for col in num_cols:
    print(col, check_outlier(df, col))
 

#Now replace these outliers with thresholds.
for col in num_cols:
    replace_with_thresholds(df, col)

#After replacing, we shouldn't have any outlier. So let's check again.
for col in num_cols:
    print(col, check_outlier(df, col))


##Feature Scaling 
df_test=df[df['Purchase'].isnull()]


df_train=df[~df['Purchase'].isnull()]



X=df_train.drop('Purchase',axis=1)

X.head()
X.shape



y=df_train['Purchase']
y.shape



y


