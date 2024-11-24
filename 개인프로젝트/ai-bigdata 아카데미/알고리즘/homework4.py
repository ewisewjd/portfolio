#!/usr/bin/env python
# coding: utf-8

# In[ ]:


t=int(input())

for _ in range(t):
    n,m=map(int, input().split())
    data=[]
    
    for i in range(n):
        data.append(list(map(int,input().split())))
        
    T=[[0]*m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                T[i][j]=data[i][j]
            elif i==0:
                T[i][j]=T[i][j-1]+data[i][j]
            
            elif j==0:
                T[i][j]=T[i-1][j]+data[i][j]
            
            else:
                max_path=max(T[i][j-1], T[i-1][j],T[i-1][j-1])+data[i][j]
                
                if i >= 2 and j >= 2:
                    max_path=max(max_path, T[i-2][j-2] + data[i][j])
                T[i][j] = max_path 
    
    print(T[n-1][m-1])

