
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


red_wine_url = "https://raw.githubusercontent.com/nishilp/DataScience01/master/Data/red_wine.csv"
white_wine_url = "https://raw.githubusercontent.com/nishilp/DataScience01/master/Data/white_wine.csv"


# In[3]:


# Get two datasets, one for red wine and other for white wine

red= pd.read_csv(red_wine_url)
white = pd.read_csv(white_wine_url)


# In[4]:


# checking the dataframes of red wine dataset using head() method

red.head(5)


# In[5]:


# checking the dataframes of white wine dataset using head() method

white.head(5)


# In[6]:


# Merge both red and white wine datasets into one

frames = [red, white]
ds = pd.concat(frames)


# In[7]:


# Check for no. of duplicate records

sum(ds.duplicated())


# In[8]:


# Remove the duplicate records using drop_duplicates() method

ds = ds.drop_duplicates()


# In[9]:


# Check total number of rows and columns. This frame has 5320 rows and 14 columns

ds.shape


# In[10]:


# Check rows with missing attribute values

ds.isnull().sum(axis=0)

# No missing attributes so no drop or filling required


# In[11]:


# Plotting few important columns
ds['fixed acidity'].plot(kind='hist')


# In[12]:


ds['total sulfur dioxide'].plot(kind='hist')


# In[13]:


ds['pH'].plot(kind='hist')


# In[14]:


ds['alcohol'].plot(kind='hist')


# In[15]:


# Alcohol seems to have the most impact on the quality of wine
# Scatter plot alcohol vs quality

ds.plot(x='quality', y='alcohol', kind='scatter')


# In[16]:


# Let us try to group data and aggregate information for all columns. For example finding mean values for all qualities

ds.groupby('quality').mean()

# Below observation clearly shows wines with alcohol% > 11 is classified as good wine


# In[17]:


# Splitting the dataset further based on the color of wine

ds.groupby(['quality','color']).mean()

# This also shows that majority of good wines have lesser 'volatile acidity' and 'chlorides'


# In[18]:


# We can find which color wine is associated with higher quality using mean()

ds.groupby('color')['quality'].mean()

# For this dataset, white wine is associated with higher quality


# In[19]:


# Using describe() method we can output properties of attributes

ds.groupby('color').describe()


# In[20]:


# Question: Do sweeter wine gets better rating ? Lets find out

low_sugar = ds[ds['residual sugar'] < 3] 
high_sugar = ds[ds['residual sugar'] >= 3]

# This shows that high sugar wine has slightly higher quality


# In[21]:


low_sugar['quality'].mean() 


# In[22]:


high_sugar['quality'].mean() 


# In[23]:


# Creating Visualizations to show wine quality associations with other properties
# ABOUT--- Q1: Is a certain type of wine (red or white) associated with higher quality?:


ax = ds.groupby('color')['quality'].mean().plot(kind='bar', title='Avg Quality by Color', color = ['red', 'white'] , alpha=0.7)
ax.set_facecolor("lightslategray")

