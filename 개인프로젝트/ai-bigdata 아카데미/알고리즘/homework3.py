#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. 라이브러리 임포트 
import sys
sys.setrecursionlimit(1000000)
from collections import deque

# 2. testcase 숫자와 입력을 받음 
t=int(input())
for _ in range(t):
    N,M=map(int,input().split()) #정점의 개수 n과 간선의 개수 m
    List=[[] for _ in range(N)]
    
    for i in range(M):
        u,v=map(int,input().split())
        List[u].append(v)
    
    for i in range(N):
        List[i].sort()
    
    check=[False]*N
    queue = deque([0])
        
        
    check[0] = True  
       
    while queue:
            
        v = queue.popleft()  
            
        print(v, end=" ")
               
          
        for i in List[v]:
            if not check[i]:
                check[i] = True
                queue.append(i) 

    print()  

