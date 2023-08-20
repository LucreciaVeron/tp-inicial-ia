#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


# In[41]:


mydataset = pd.read_csv("../tp inicial/2022-new.csv")
mydataset


# In[ ]:





# In[19]:


mydataset.keys()


# In[21]:


mydataset['departamento_id']


# In[23]:


mydataset[['departamento_nombre', 'cantidad_casos']]


# In[32]:


mydataset.plot.scatter(x='cantidad_casos', y='provincia_nombre')
plt.show()


# In[33]:


mydataset.plot.scatter(x='cantidad_casos', y='departamento_nombre')
plt.show()


# In[42]:


agrupado_suma = mydataset.groupby('departamento_nombre')['cantidad_casos'].sum()
print(agrupado_suma)


# In[38]:


agrupado_suma = mydataset.groupby('provincia_nombre')['cantidad_casos'].sum()
print(agrupado_suma)


# In[43]:


agrupado_suma = mydataset.groupby('grupo_edad_desc')['cantidad_casos'].sum()
print(agrupado_suma)


# In[30]:


mydataset.head()


# In[ ]:





# In[31]:


x = mydataset.values
print (x)


# In[34]:


casos_departamento = mydataset[['departamento_nombre', 'cantidad_casos']].values
print (casos_departamento)


# In[ ]:




