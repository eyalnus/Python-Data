#!/usr/bin/env python
# coding: utf-8

# # Exploring Data
# Here we will look at some basic exploration of data sets.

# In[ ]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install numpy')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[ ]:


diamonds = pd.read_csv('diamonds.csv', index_col='#')
diamonds.head()


# * carat - The weight of a diamond is measured in carats. In fact, all gemstones are measured in this fashion. Carat weight is made up of points. It takes 100 points to equal 1 carat. For example, 25 points = 1/4 carat, 50 points = 1/2 carat, etc. Of course, the higher the carat weight of the diamond, the more you can expect to pay for it. 
# * cut - A diamond cut is a style or design guide used when shaping a diamond for polishing. Cut does not refer to shape (pear, oval), but the symmetry, proportioning, and polish of a diamond. The cut of a diamond greatly affects a diamond’s brilliance; this means if it is cut poorly, it will be less luminous. This variable focuses on a judgment about the quality of the diamond’s cut: Fair; Good; Very Good; Premium; Ideal.
# * color - Most commercially available diamonds are classified by color, or more appropriately, the lack of color. The most valuable diamonds are those classified as colorless, yet there are stones that have rich colors inluding yellow, red, green and even black that are extremely rare and valuable. Color is graded on a letter scale from D to Z, with D representing a colorless diamond.
# * clarity - The clarity of a diamond is determined by the number, location and type of inclusions it contains. Inclusions can be microscopic cracks, mineral deposits, or external markings. Clarity is rated using a scale which contains a combination of letters and numbers to signify the amount and type of inclusions. This scale ranges from FL to I3, FL being Flawless and the most valuable. 
# * x - Length of the diamond in millimeters.
# * y - Width of the diamond in millimeters.
# * z - This variable is a measure of the height in millimeters measured from the bottom of the diamond to its table (the flat surface on the top of the diamond); also called depth of the diamond.
# * depth - This variable is the depth total percentage of the diamond defined by 2(z) / (x + y).
# * table - This variable is a measure of table width, the width of top of diamond relative to widest point.
# * price - The retail price of the diamond in U.S. dollars.

# In[ ]:


diamonds.info()


# In[ ]:


diamonds.describe(include="all")


# In[ ]:


sns.histplot(diamonds.price, bins=100, kde=True)


# In[ ]:


sns.histplot(np.log(diamonds.price), bins=100, kde=True)


# In[ ]:


sns.histplot(diamonds.carat, bins=100, kde=False)


# In[ ]:


diamonds.carat.value_counts().head(10)


# In[ ]:


sns.histplot(diamonds.carat.round(1), bins=100, kde=False)


# In[ ]:


sns.histplot(diamonds.table, bins=100, kde=False)


# In[ ]:


sns.histplot(diamonds.depth, bins=100, kde=False)


# In[ ]:


sns.jointplot(x='x', y='y', data=diamonds, xlim=[0, 10], ylim=[0,10])


# > **Observations:** 
# * There are several non-round-cut diamonds
# * There are some very small diamonds and some zeros.
# 
# For better visualization, we remove non-round-cut and tiny diamonds.

# In[ ]:


diamonds = diamonds.loc[((diamonds.y-diamonds.x).abs()<0.1) & (diamonds.x>1)]


# In[ ]:


sns.jointplot(x='x', y='y', data=diamonds)


# ### Does weight and size affect price?

# In[ ]:


sns.jointplot(x='carat', y='price', kind='scatter', data=diamonds)


# > **Conclusion:** The carat is an influencial feature, but...
# * the influence is not linear (slope)
# * other features have significant influence (width)

# In[ ]:


diamonds.head()


# In[ ]:


sns.scatterplot(x='x', y='price', data=diamonds)


# > This looks very similar to the analysis based on the carat. What about other size features?

# In[ ]:


sns.scatterplot(x='z', y='price', data=diamonds)


# > Does the height appear to be a contributing factor? 

# In[ ]:


sns.jointplot(x='depth', y='price', kind='scatter', data=diamonds)


# In[ ]:


sns.jointplot(x='table', y='price', kind='scatter', data=diamonds)


# > What about symmetry?

# In[ ]:


diamonds.head()


# In[ ]:


diamonds['symmetry'] = diamonds['x']/diamonds['y'] # add symmetry of x/y to dataframe


# In[ ]:


sns.jointplot(x='symmetry', y='price', kind='scatter', data=diamonds)


# > What does this graph tell you about how x and y are chosen to length and width?

# ### Correlaiton Plot
# The most familiar measure of dependence between two quantities is the Pearson product-moment correlation coefficient.
# It is obtained by taking the ratio of the covariance of the two variables in question of our numerical dataset, normalized to the square root of their variances: corr(x,y) = cov(x,y)/(std(x)\*std(y)). A correlation near 1 or -1 means highly correlated, a correlation near 0 means independently distributed. The sign of the correlation defines the relationship. Positive values show that an increase in 'x' corresponds to and increase in 'y' and vice versa. A negative relationship shows that an increase in 'x' corresponds to a decrease in 'y' and vice versa.

# In[ ]:


df = diamonds.select_dtypes(np.number)
corrMatrix = df.corr()
print(corrMatrix)


# In[ ]:


sns.heatmap(corrMatrix, annot=True)
plt.show()


# > Despite what our graph showed, it appears there is high correlation between 'z' and price. What did we miss?

# In[ ]:


diamonds = diamonds.loc[(diamonds.z<30) & (diamonds.z>0)]
sns.jointplot(x='z', y='price', data=diamonds)


# > The outliers skewed our perspective.

# ## Categorical Features
# Categorical features need different plot types such as bar and violin plots.

# In[ ]:


vp = sns.violinplot(x='price', 
                    data=diamonds)


# In[ ]:


print(diamonds.cut.unique())


# In[ ]:


cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
diamonds.cut.value_counts().reindex(cut_order).plot.bar()


# In[ ]:


vp = sns.violinplot(x='cut', y='price', 
                    order=cut_order, 
                    data=diamonds)


# In[ ]:


vp = sns.violinplot(x='cut', y='x', 
                    order=cut_order, 
                    data=diamonds)


# In[ ]:


vp = sns.violinplot(x='x', 
                    data=diamonds)


# In[ ]:


print(diamonds.color.unique())


# In[ ]:


color_order = diamonds.color.unique().tolist()
color_order.sort()
print(color_order)


# In[ ]:


diamonds.color.value_counts().reindex(color_order).plot.bar()


# In[ ]:


vp = sns.violinplot(x='color', y='price', 
                    order=color_order, 
                    data=diamonds)


# > **Conclusion:** The color is an influencial feature on the price.
# 

# # Log Transform - Brain Sizes

# In[ ]:


brain = pd.read_csv('brain.csv', index_col='Animal')
sns.jointplot(x='Body Weight', y='Brain Weight', kind='scatter', data=brain)


# In[ ]:


brain["log Brain"] = np.log(brain["Brain Weight"])
brain["log Body"] = np.log(brain["Body Weight"])
sns.jointplot(x='log Body', y='log Brain', kind='scatter', data=brain)


# # Video Game Sales

# In[ ]:


games =  pd.read_csv('vgsales.csv', index_col='Rank')


# In[ ]:


games.describe()


# In[ ]:


games.head(15)


# In[ ]:


games['Genre'].value_counts()


# In[ ]:


plt.figure(figsize=(15, 10))
sns.countplot(x="Genre", data=games, order = games['Genre'].value_counts().index)
plt.xticks(rotation=90)


# In[ ]:


data_year = games.groupby(by=['Year'])['Global_Sales'].sum()
data_year = data_year.reset_index()
plt.figure(figsize=(15, 10))
sns.barplot(x="Year", y="Global_Sales", data=data_year)
plt.xticks(rotation=90)


# In[ ]:


platform = pd.pivot_table(games.loc[(games.index<=100)],columns="Platform", aggfunc=np.sum)
platform.head()


# # Sales Histogram

# In[ ]:


plt.figure(figsize=(25,30))
sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
for i, column in enumerate(sales_columns):
    plt.subplot(3,2,i+1)
    sns.histplot(games[column], bins=20, kde=True)


# In[ ]:


data_hist_log = games.copy()
# create log of sales data and remove 0s
data_hist_log = data_hist_log[data_hist_log.NA_Sales != 0]
data_hist_log = data_hist_log[data_hist_log.EU_Sales != 0]
data_hist_log = data_hist_log[data_hist_log.Other_Sales != 0]
data_hist_log = data_hist_log[data_hist_log.JP_Sales != 0]
data_hist_log = data_hist_log[data_hist_log.Global_Sales != 0]
# plot data
plt.figure(figsize=(25,30))
sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
for i, column in enumerate(sales_columns):
    plt.subplot(3,2,i+1)
    sns.histplot(np.log(data_hist_log[column]), bins=20, kde=True)


# In[ ]:




