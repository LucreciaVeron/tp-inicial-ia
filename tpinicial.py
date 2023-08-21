#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


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


# In[66]:


mydataset.plot.scatter(x='cantidad_casos', y='provincia_nombre')
plt.show()


# In[33]:


mydataset.plot.scatter(x='cantidad_casos', y='departamento_nombre')
plt.show()


# In[44]:


mydataset.plot.scatter(x='semanas_epidemiologicas', y='cantidad_casos')
plt.show()


# In[72]:


agrupado_semanas = mydataset.groupby('semanas_epidemiologicas')['cantidad_casos'].sum()
print(agrupado_semanas)


# In[70]:


agrupado_departamento = mydataset.groupby('departamento_nombre')['cantidad_casos'].sum()
print(agrupado_departamento)


# In[71]:


agrupado_provincia = mydataset.groupby('provincia_nombre')['cantidad_casos'].sum()
print(agrupado_provincia)


# In[69]:


agrupado_edad = mydataset.groupby('grupo_edad_desc')['cantidad_casos'].sum()
print(agrupado_edad)


# In[77]:


ejemplo = np.array(agrupado_departamento)
print(ejemplo)


# In[75]:


ejemplo2 = mydataset.groupby(['departamento_nombre', 'cantidad_casos'])
print(ejemplo2)


# In[30]:


mydataset.head()


# In[62]:


mydataset = pd.DataFrame(mydataset)


# In[31]:


x = mydataset.values
print (x)


# In[67]:





# In[88]:


departamentos = np.array(mydataset['departamento_id'])
print(departamentos)


# In[57]:


cantidad = np.array(mydataset['cantidad_casos'])
print(cantidad)


# In[82]:


regresion_logistica = LogisticRegression()
regresion_logistica.fit(departamentos,cantidad)


# In[ ]:




