#!/usr/bin/env python
# coding: utf-8

# In[4]:


l = float(input("Enter the wavelength: "))


# In[5]:


nowsq = 2.7359 + 0.01878 / (l**2 - 0.01822) - 0.01354 * l**2
no2wsq = 2.7359 + 0.01878 / ((2*l)**2 - 0.01822) - 0.01354 * (2*l)**2
ne2wsq = 2.3753 + 0.01224 / ((2*l)**2 - 0.01667) - 0.01516 * (2*l)**2


# In[6]:


print(nowsq)
print(no2wsq)
print(ne2wsq)


# In[22]:


import numpy as np


# In[12]:


step1 = no2wsq * ne2wsq / nowsq


# In[13]:


print(step1)


# In[14]:


step2 = ne2wsq - step1


# In[15]:


print(step2)


# In[17]:


step3 = step2 / (ne2wsq - no2wsq)


# In[18]:


print(step3)


# In[23]:


step4 = np.sqrt(step3)


# In[ ]:




