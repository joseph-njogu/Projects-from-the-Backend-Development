#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier  

data = pd.read_csv("music.csv")
x = data.drop(columns=["genre"])
y = data["genre"]
model = DecisionTreeClassifier()
model.fit(x,y)
predictions = model.predict([[21,1],[22,0]])
predictions


# In[ ]:




