#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
model = DecisionTreeClassifier()
data = pd.read_csv('music.csv')
x=data.drop(columns=['genre'])
y=data['genre']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1)
model.fit(x_train,y_train)
prediction=model.predict(x_test)
accuracy=accuracy_score(y_test,prediction)
accuracy



# In[ ]:




