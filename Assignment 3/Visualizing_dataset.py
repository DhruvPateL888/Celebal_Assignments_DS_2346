#Username : CT_CSI_DS_2346
#Name : Dhruv Patel

# Importing the Libraries
import pandas as pd
import numpy as np
from sklearn import preprocessing
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
sns.set_style('whitegrid')

#__ Loading the Dataset__
df = pd.read_csv('Placement_Data_Full_Class.csv')

#Viewing Dataset
df.head(10)
print()
df.info()
print()

#__Data Preprocessing__
df.drop('sl_no', inplace = True, axis = 1)
df.isnull().sum()

#__Dataset after Preprocessing__
df.describe()
print()

#__Placement Statistics__
placed_members = len(df[df['status'] == "Placed"])
unplaced_members = len(df[df['status'] == 'Not Placed'])
x = np.zeros(2)
x[0] = placed_members
x[1] = unplaced_members
print("Placed_members Count : ",placed_members )
print("Unplaced_members Count : ",unplaced_members )
print()
plt.title('Placement Status')
plt.pie(x, labels = ['no_placed_members', 'no_unplaced_members'],shadow =True)
plt.show()
print()
print()

#__Gender Destribution__
male_count = len(df[df['gender'] == 'M'])
female_count = len(df[df['gender'] == 'F'])
x = np.zeros(2)
x[0] = male_count
x[1] = female_count
print("Male Count : ",male_count )
print("Female Count : ",female_count )
print()
plt.title('Gender Distribution')
plt.pie(x, labels = ['Male', 'Female'],shadow =True)
plt.show()
print()
print()

sns.boxplot(x = 'salary', y = 'gender', data = df)
plt.title('Boxplot of Salary by Gender')
plt.show()
print()

df.groupby(["gender","status"]).size().groupby(level=0, group_keys = False).apply( lambda x: 100 * x / x.sum()).unstack().plot(kind='bar',stacked=True)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.legend(loc = 'upper right',title = 'Status')
plt.title("Comparision of placement of male and female")
plt.xlabel('Gender')
plt.show()
print()
print()

#__Effects of Secondary education on placement and salary__

sns.catplot(x = 'status', y = 'ssc_p', hue = 'gender', data = df)
plt.title("Visualizing the ssc percentages")
plt.xlabel('Staus')
plt.ylabel('Secondary Education percentage')
plt.show()
print()


sns.countplot(x = 'ssc_b', hue='status', data = df)
plt.title('Count of Boards of Secondary Education')
plt.xlabel('Boards')
plt.ylabel('Counts')
plt.show()
print()

df.groupby('ssc_b')['status'].value_counts(normalize=False)
print()
print()
sns.boxplot(x = 'salary', y = 'ssc_b', data = df)
plt.title('Boxplot of salary by Board of Secondary Education')
plt.ylabel('Boards')
plt.xlabel('Salary')
plt.show()

print()
sns.regplot(x = 'ssc_p', y = 'salary', data = df)
plt.title("Relation of SSC percentage with the salary")
plt.xlabel('Secondary Education Percentage')
plt.ylabel('Salary')
plt.show()
print()


#__Effects of Higher Secondary education on placement and salary__
sns.catplot(x = 'status', y = 'hsc_p', hue = 'gender', data = df)
plt.xlabel('Staus')
plt.title("Visualizing the HSC percentages")
plt.ylabel('Higher Secondary Education percentage')
plt.show()
print()

sns.countplot(x = 'hsc_b', hue='status', data = df)
plt.title('Count of Boards of Higher Secondary Education')
plt.xlabel('Boards')
plt.ylabel('Counts')
plt.show()
print()
print()

df.groupby('hsc_b')['status'].value_counts(normalize=False)
print()

sns.boxplot(x = 'salary', y = 'hsc_b', data = df)
plt.title('Boxplot of Salary by Higher Secondary Boards')
plt.xlabel('Salary')
plt.ylabel('Higher Secondary Boards')
plt.show()
print()

sns.regplot(x = 'hsc_p', y = 'salary', data = df)
plt.title("Relation of HSC percentage with the salary")
plt.xlabel('Higher Secondary Education Percentage')
plt.ylabel('Salary')
plt.show()
print()

#__Effect of Work Experience on placement and salary__

df.groupby(["workex","status"]).size().groupby(level=0, group_keys=False).apply( lambda x: 100 * x / x.sum()).unstack().plot(kind='bar',stacked=True)
plt.title("Effect of Work Experience on placement")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.legend(loc = 'upper right',title = 'Work experience')
plt.xlabel('Work Experience')
plt.show()
print()

ax = sns.countplot(x = 'workex', hue = df.gender, data = df)
totals = []
for i in ax.patches:
    totals.append(i.get_height())
total = sum(totals)
for i in ax.patches:
    ax.text(i.get_x()--.1, i.get_height()+.5, \
            str(round(i.get_height(), 2)), fontsize=15,
                color='red')
plt.title("Work Trends")
plt.show()
print()


#__Specialization impact on Placement__
df.groupby(["specialisation","status"]).size().groupby(level=0, group_keys = False).apply( lambda x: 100 * x / x.sum()).unstack().plot(kind='bar',stacked=True)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.legend(loc = 'upper right',title = 'specialisation')
plt.title("effect of Specialization on placements")
plt.show()
print()

#__Relation of the percentage of degree and in MBA__
sns.regplot(x = 'degree_p', y = 'salary', data = df)
plt.xlabel('Degree Percentage')
plt.title("Relation between percentage in degree course and salary")
plt.ylabel('Salary')
plt.show()
print()


sns.regplot(x = 'mba_p', y = 'salary', data = df)
plt.xlabel('MBA Percentage')
plt.title("Relation between percentage in MBA course and salary")
plt.ylabel('Salary')
plt.show()
print()
