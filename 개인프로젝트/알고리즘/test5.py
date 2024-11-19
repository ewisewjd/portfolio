#!/usr/bin/env python
# coding: utf-8

# In[13]:


def fibo(n):
    if n<=2:
        return 1
    return fibo(n-1)+fibo(n-2)

t=int(input())

for _ in range(t):
    n=int(input())
    print(fibo(n))
    


# In[ ]:




