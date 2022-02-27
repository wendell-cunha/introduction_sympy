#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as smp
from sympy import *


# In[2]:


x = smp.symbols('x','y')


# In[3]:


x**2


# In[4]:


smp.exp(x)


# In[6]:


smp.log(x,10)


# In[11]:


smp.sin(x/2 + smp.sin(x))


# In[15]:


smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi)


# In[16]:


(smp.cos(x)-1)/x


# In[19]:


smp.limit((smp.cos(x)-1)/x, x,smp.oo)


# In[24]:


integrate(1/x, x)


# In[25]:


conda install mpmath


# In[ ]:




