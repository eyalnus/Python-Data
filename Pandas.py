#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install numpy')
get_ipython().system('pip install seaborn')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Pandas
# Pandas is a Python library focused on data manipulation and analysis. It can be seen as an extension of NumPy, and is based on the NumPy `ndarray`, `dtype` and corresponding functionalities. Pandas offers data structures and operations for manipulating tabular data and time series. Pandas introduces 2 new data structure - `Series` and `DataFrame`. 

# ## Series
# The `Series` structure is similar to the 1-dimensional NumPy array, with the addition of an *index* attribute. It can be created from `list`s, `ndarray`s and similar objects. As with `ndarray`, all items must be of the same `dtype`.

# In[ ]:


simple_series = pd.Series(list("abcdefg"))
print(simple_series)


# *Note: by default, a `Series` is given an index of sequential numbers starting from 0*

# In[ ]:


print(simple_series.index)
print(simple_series.values)


# ### `Series` index

# ##### Accesing `Series` by index

# In[ ]:


simple_series[0]
simple_series[2:5]


# ##### Manual `Series` index

# In[ ]:


indexed_series = pd.Series(np.linspace(0.,2.,9), index = list('abcdefghi'))
print(indexed_series)


# In[ ]:


print("indexed_series['b']:",indexed_series['b'])
print("indexed_series[1]:",indexed_series[1])
print("indexed_series['c':'h']:\n",indexed_series['c':'h'])
print("indexed_series[3:8]:\n",indexed_series[2:7])


# In[ ]:


indexed_series.index = [i for i in range(0,18,2)]
print(indexed_series)


# In[ ]:


print("indexed_series[0]:",indexed_series[0])
print("indexed_series[2]:",indexed_series[2])
print("indexed_series[2:7]:\n",indexed_series[2:7])


# In[ ]:


#print("indexed_series[1]:",indexed_series[1])


# *Accessing `Series` elements using the square brackets `[]` operator can be confusing and inconsistent when the index is not a sequential range. Use `loc` and `iloc` instead.*

# In[ ]:


print(indexed_series.loc[2]) #access by Series index (index location)
print(indexed_series.iloc[2]) #acces by Series item number (integer location)


# In[ ]:


print(indexed_series.loc[2:8]) 
print(indexed_series.iloc[2:8]) 


# In[ ]:


indexed_series.loc[0] = -1
print(indexed_series)


# In[ ]:


indexed_series.loc[2:4] = -2
print(indexed_series)


# In[ ]:


indexed_series.loc[6:12] = [0,0.25,.75,1]
print(indexed_series)


# In[ ]:


ascii_series = pd.Series({"a":97, "b":98,"c":99,"d":100,"A":65, "B":66,"C":67,"D":68})
print(ascii_series)


# In[ ]:


ascii_series.loc['E'] = 69
ascii_series.loc['e'] = 101
print(ascii_series)


# In[ ]:


expanded_series = pd.Series({"f":102, "g":103,"h":104,"i":105,"F":70, "G":71,"H":72,"I":73})
ascii_series = ascii_series.append(expanded_series)
print(ascii_series)
print("******")
print(ascii_series.loc['a':'f'])


# In[ ]:


ascii_series.sort_index(inplace=True)
print(ascii_series)
print("******")
print(ascii_series.loc['a':'f'])


# # DataFrame
# The Pandas `DataFrame` is used to hold tabular data (tables, similar to SQL or Excel). It can be seen as a 2-dimensional `ndarray` where the columns are an ordered sequence of aligned `Series` objects (sharing the same index). It can also be seen as a specialized version of the Python `dict` object, where the keys are column names and values are the `Series` mapped to each name.

# In[ ]:


unicode_series = pd.Series(dict(zip(list("ABCDEFGHIabcdefghi"),[i for i in range(41,50)]+[i for i in range(61,70)])))
print(unicode_series)


# In[ ]:


df = pd.DataFrame({'ascii':ascii_series,'unicode':unicode_series})
df


# In[ ]:


print(df.index)
print(df.columns)


# ##### Accessing a DataFrame

# In[ ]:


df['ascii'] #index by columns


# In[ ]:


df.unicode #columns as attributes


# *Note: accessing via attribute method can be dangerous if the column name corresponds to an existing attribute or function of the DataFrame object. In this case, the object's attribute will be returned (or modified!) instead of the column. It is safest to use the indexing access method.*

# In[ ]:


df.values


# In[ ]:


df["A":"a"] #despite indexing by columns, slicing is done by index


# In[ ]:


df[0:9] # or slice by row number


# In[ ]:


df[df.ascii > 70]


# In[ ]:


print(df.ascii > 70)
print (type(df.ascii > 70))


# ###### Boolean operators on DataFrame columns create a `Series` of boolean values, mapping DF indices to the results of the boolean test.

# ### DateFrame Views

# In[ ]:


df.T # transposed view


# *Note: as with NumPy arrays, some functions for Series and DataFrames return a reference (view), and some return a copy. Modifying views will modify the original object.*

# In[ ]:


print(df.head())
print(df.tail())


# In[ ]:


head = df.head()
head['ascii']['A'] = 0
print(df)


# In[ ]:


df.T['A']['ascii'] = 65
print(df)


# In[ ]:


df['lower'] = df.index.str.lower()
print(df.head())


# In[ ]:


df['order'] = df['lower'].apply(ord) - ord('a') + 1
print(df)


# In[ ]:


df.drop('lower',1,inplace=True)
print(df)


# ### `loc` and `iloc` in DataFrames
# In `DataFrame`s, the `loc` and `iloc` access by index and sequence number respectively. The accessor accepts 2 indicers, the first being the row and the second being the column.

# In[ ]:


df.loc['A','ascii']


# In[ ]:


df.loc['A',['ascii','order']]


# In[ ]:


df.loc['A':'E',['ascii','order']]


# In[ ]:


df.iloc[1,2] # row 1, column 2


# In[ ]:


df.iloc[6:,-1] # row 6:end, last column


# In[ ]:


df.iloc[1:4,1:3] #row 1-3, column 1-2


# # Working Example - Sea Ice

# In[ ]:


sea_ice = pd.read_csv('sea-ice-fixed.csv',index_col='Date') # explicitly define column as index
sea_ice.head()


# In[ ]:


sea_ice.index = pd.to_datetime(sea_ice.index)
sea_ice.head()


# In[ ]:


sea_ice[sea_ice.index > '1980'].head(10)


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
sea_ice.groupby('hemisphere').plot(ax=ax)


# In[ ]:


fig=plt.figure(figsize=(12, 6))
north = sea_ice[sea_ice.hemisphere == "north"]
south = sea_ice[sea_ice.hemisphere == "south"]
plt.plot(north.index,north.Extent,label='Northern Hemisphere')
plt.plot(south.index,south.Extent,label='Southern  Hemisphere')
plt.legend(bbox_to_anchor=(0., -.362, 1., .102), loc=3, ncol=2, 
           mode="expand", borderaxespad=0.)


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
for name, group in sea_ice.groupby('hemisphere'):
    group.plot(y="Extent", ax=ax, label=name)


# #### Resampling
# When using a datetime index we can "resample" the data over a time period. This allows us to aggregate the data by days, months, years or even minutes and seconds (if we have that level of resolution).

# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
for name, group in sea_ice.groupby('hemisphere'):
    group.resample('1M').mean().plot(y="Extent", ax=ax)


# In[ ]:


fig, axs = plt.subplots(6,1,figsize=(12,32))
for name, group in sea_ice.groupby('hemisphere'):
    for i in range(1,7):
        group.resample(str(i*2)+'M').mean().plot(y="Extent", ax=axs[i-1])


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
for name, group in sea_ice.groupby('hemisphere'):
    group.resample('14D').mean().plot(y="Extent", ax=ax)


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
for name, group in sea_ice.groupby('hemisphere'):
    group.resample('1M').count().plot(y="Extent", ax=ax, label=name)


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
for name, group in sea_ice[(sea_ice.index <= '1989') & (sea_ice.index >= '1987')].groupby('hemisphere'):
    group.resample('2D').count().plot(y="Extent", ax=ax, label=name)


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
for name, group in sea_ice[(sea_ice.index <= '1989') & (sea_ice.index >= '1987')].groupby('hemisphere'):
    group.resample('14D').mean().plot(y="Extent", ax=ax, label=name)


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
for name, group in sea_ice[(sea_ice.index <= '1988-01-15') & (sea_ice.index >= '1987-11-25')].groupby('hemisphere'):
    group.resample('1D').count().plot(y="Extent", ax=ax, label=name)


# In[ ]:


sea_ice[(sea_ice.index <= '1988-01-13') & (sea_ice.index >= '1987-12-02')]


# ##### Grouping by multiple columns

# In[ ]:


monthly = sea_ice.groupby(["hemisphere",sea_ice.index.month])
mon_mean = monthly.mean()
mon_mean


# In[ ]:


mon_mean.index


# In[ ]:


mon_mean.loc['north']


# In[ ]:


mon_mean.loc[("north",3):("south",3)]


# In[ ]:


for name, group in mon_mean.groupby("hemisphere"):
        print(group)


# In[ ]:


mon_mean.unstack(level=0)


# ###### This effectively gives us a pivot table

# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))
mon_mean.unstack(level=0)['Extent'].plot(ax=ax)


# ### Pivot Tables

# In[ ]:


titanic = pd.read_csv('titanic.csv', index_col='PassengerId')
titanic.head()


# * Pclass = socia-economic status (upper/middle/lower)
# * SibSp = # of siblings/spouses on board
# * Parch = # of parents/children on board
# * Embarked = port of embarkation, Cherbourgh,Queenstown or southampton

# In[ ]:


titanic.drop(['Name','Ticket'],axis=1,inplace=True)
titanic.head(10)


# In[ ]:


titanic.tail(10)


# ##### Let's look at survival status with regards to gender, using groupby

# In[ ]:


titanic.groupby('Sex')[['Survived']].mean()


# ###### This is useful, and already grants some insight, but let's dive deeper and also examine passenger class

# In[ ]:


titanic.groupby(['Sex', 'Pclass'])['Survived'].aggregate('mean').unstack()


# *As we can see this is a very useful method for understanding the data, but the syntax can get quite cumbersome. This is where the pivot table comes in handy.*

# In[ ]:


titanic.pivot_table('Survived', index='Sex', columns='Pclass')
# Survived is the column to aggregate, by default aggregation is done using the 'mean' function.
# columns defines which columns will be the grouper


# In[ ]:


titanic.pivot_table('Survived', index='Sex', columns='Pclass', margins=True)


# In[ ]:


age = pd.cut(titanic['Age'], [0, 18, 80]) # cut gives us a distribution of numeric values into bins
titanic.pivot_table('Survived', ['Sex', age], 'Pclass') # multi index


# In[ ]:


fare = pd.qcut(titanic['Fare'], 2)
titanic.pivot_table('Survived', ['Sex', age], [fare, 'Pclass'])


# In[ ]:


fare4 = pd.qcut(titanic['Fare'], 4)
titanic.pivot_table('Survived', ['Sex', age], [fare4, 'Pclass'],aggfunc='sum')


# *We can also choose which aggregation functions are used for each column*

# In[ ]:


titanic.pivot_table(index='Sex', columns='Pclass',
                    aggfunc={'Survived':sum, 'Fare':'mean'})


# In[ ]:


corr=titanic.corr()
corr


# In[ ]:


mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(8, 6))
cmap = sns.diverging_palette(200, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5)


# #### One-Hot Encoding
# One-Hot encoding takes categorical data and transforms it into a boolean vector, where each value in the vector will be 0, except for the one representing the category index of the data.
# For example, if we have a categorical feature with values [red,blue,green] we can transform it into 3 numerical features, red, blue and green, and each entity will be marked with a '1' in the corresponding column, and 0 in the others. In `Pandas` this is done using the `get_dummies()` function.

# In[ ]:


pd.get_dummies(titanic['Sex'])


# In[ ]:


titanic_oh = pd.concat([titanic,pd.get_dummies(titanic['Sex'])],axis=1)
titanic_oh.head(10)


# In[ ]:


titanic_oh = pd.concat([titanic_oh,pd.get_dummies(titanic['Embarked'])],axis=1)
titanic_oh.head(10)


# In[ ]:


corr_oh = titanic_oh.corr()
corr_oh


# In[ ]:


mask = np.triu(np.ones_like(corr_oh, dtype=bool))
f, ax = plt.subplots(figsize=(8, 6))
cmap = sns.diverging_palette(200, 10, as_cmap=True)
sns.heatmap(corr_oh, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5)


# In[ ]:


titanic_oh["Cabin"]


# In[ ]:


titanic_oh["Cabin"].dropna()


# In[ ]:


titanic_oh["Cabin"].dropna().str[0]


# In[ ]:


np.unique(titanic_oh["Cabin"].dropna().str[0])


# In[ ]:


titanic_oh["Deck"] = titanic_oh["Cabin"].dropna().str[0]
titanic_oh.head()


# In[ ]:


titanic_oh = pd.concat([titanic_oh,pd.get_dummies(titanic_oh['Deck'],prefix="D")],axis=1)
corr_oh = titanic_oh.corr()
corr_oh


# In[ ]:


mask = np.triu(np.ones_like(corr_oh, dtype=bool))
f, ax = plt.subplots(figsize=(8, 6))
cmap = sns.diverging_palette(200, 10, as_cmap=True)
sns.heatmap(corr_oh, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5)


# In[ ]:




