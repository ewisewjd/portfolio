#!/usr/bin/env python
# coding: utf-8

# In[7]:


t=int(input())
for _ in range(t):
    n=int(input())
    fib=[0]*(n+1)
    
    for i in range(1,n+1):
        if i==1 or i==2:
            fib[i]=1
        
        else:
            fib[i]=fib[i-1]+fib[i-2]

    
    print(fib[n])
    
#     for i in range(n):
#         total+= n-1+n-2
#         if n==1 or n==2:
#             total=1
#         print(total)


# In[ ]:




