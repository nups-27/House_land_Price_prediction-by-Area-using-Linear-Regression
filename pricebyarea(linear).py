#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

file1=pd.read_csv("Book1.csv")
print(file1)


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel("Area in sq ft")
plt.ylabel("price in rs")
plt.scatter(file1.Area,file1.price)


# In[13]:


reg=linear_model.LinearRegression()
reg.fit(file1[["Area"]],file1.price)
coefficient=reg.coef_
print("coefficient of regression :",coefficient)
intercept=reg.intercept_
print("intercept of line ;",intercept)
new_data=pd.DataFrame({'Area':[3800]})
predicted_price=reg.predict(new_data)
print("predicted price according to area is:",predicted_price)
      
143.52941176+3800+156705.8823429411      


# In[ ]:




