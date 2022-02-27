#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)


# In[2]:


solveset(Eq(x**2, 1), x)


# In[3]:


solveset(Eq(x**2, 1), x)


# In[5]:


solveset(x - x, x,)


# In[6]:


solveset(sin(x) - 1, x, domain=S.Reals)


# In[7]:


linsolve(Matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z))


# In[8]:


solve([x**2 - y**2/exp(x)], [x, y], dict=True)


# In[9]:


f, g = symbols('f g', cls=Function)


# In[12]:


diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
dsolve(diffeq, f(x))


# In[13]:


dsolve(f(x).diff(x)*(1 - sin(f(x))) - 1, f(x))


# In[ ]:




