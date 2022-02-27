#!/usr/bin/env python
# coding: utf-8

# #Introduction to SymPy

# In[3]:


from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)


# In[4]:


diff(cos(exp(x)), x)


# In[6]:


diff(cos(exp(x**2)),x ,x,x)


# Podemos também fazer derivadas parciais

# In[9]:


f = exp(x*(y)**2)**cos(z)
diff(f, z, x, x)


# Também é possível fazer integrais

# In[10]:


integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


# In[16]:


integrate(exp(x)*cos(x**2) ,x)


# In[17]:


integrate(exp(x)*cos(x**2)*x ,x)


# In[18]:


integ = Integral(x**y*exp(-x), (x, 0, oo))


# In[9]:


from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)


# In[12]:


exp(x**2).series(x, x0=8.5)


# In[ ]:




