#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
data = pd.read_csv('music.csv')
x=data.drop(columns=['genre'])
y=data['genre']

model=DecisionTreeClassifier()
model.fit(x,y)
tree.export_graphviz(model,out_file='musicrecomender.dot',
                    feature_names=['age','gender'],
                    class_names=sorted(y.unique()),
                    label='all',
                    rounded=True,
                    filled=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




