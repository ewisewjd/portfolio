#!/usr/bin/env python
# coding: utf-8

# In[1]:


import collections


# In[3]:


t=int(input())

for _ in range(t):
    queue=collections.deque([])
    answer=[]
    qry=list(map(int, input().split()))
    for q in qry:
        if q>0:
            queue.append(q)
        elif q== -1:
            answer.append(queue.popleft())
        else: 
            pass
        
    print(*answer)


# In[ ]:




