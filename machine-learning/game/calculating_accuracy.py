#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("music.csv")
x = data.drop(columns=["genre"])
y = data["genre"]
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.9)
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
# predictions = model.predict([[21,1],[22,0]])
# predictions
predictions = model.predict(x_test)
acc = accuracy_score(y_test,predictions)
acc


# In[ ]:


[]

