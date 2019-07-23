#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
data=pd.read_csv('music.csv')
data


# In[7]:


x=data.drop(columns=['genre'])
y=data['genre']
model.fit(x,y)
predict=model.predict([[21,1],[22,0]])
predict


# In[ ]:




