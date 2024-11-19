#!/usr/bin/env python
# coding: utf-8

# In[3]:


t=int(input())

for _ in range(t):
    l=list(map(int, input().split()))
    ls=[]
    for i in l:
        
        if i >0:
            ls.append(i)
        elif i== -1:
            print(ls.pop(), end=" ")
        else:
            pass
        
        


# In[ ]:




