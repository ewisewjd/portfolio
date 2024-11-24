#!/usr/bin/env python
# coding: utf-8

# In[43]:


t=int(input())
for _ in range(t):
    gamja=list(map(int,input().split()))
    check=[]
    total_count=0
    
    for i in gamja:
        if i !=-1:
            check.append(i)
        else:
            for j in check[-5:]:
                check.pop()
                if j<=20 or j>=80:
                    total_count+=1
                    
    print(total_count)


# In[ ]:





# In[ ]:




