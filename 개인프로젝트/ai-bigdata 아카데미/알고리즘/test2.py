#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Sum(l):
    s=0
    for i in l:
        s=s+i
    return s

t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    print(sum(a))


# In[ ]:




