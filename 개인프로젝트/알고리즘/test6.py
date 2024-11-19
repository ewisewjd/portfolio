#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binarySearch(data,left,right,q): #data의 left:right 범위 내에서 q의 위치를 반환하는 함수
    if left>right:
        return -1
    
    mid=(left+right)//2 #중간 위치의 값 설정
    if data[mid]==q:
        return mid
    
    # 문제 분할 q와 data[mid]관계에 따라 부분 문제를 호출 
    if data[mid]>q:
        subproblem=binarySearch(data,left,mid-1,q)
    elif data[mid]<q:
        subproblem=binarySearch(data,mid+1,right,q)
    return subproblem

t=int(input())
for _ in range(t):
    data=list(map(int, input().split()))
    query=list(map(int, input().split()))
    answer=[]
    
    for q in query:
        answer.append(binarySearch(data,0,len(data)-1,q))
        
    print(*answer)
    
    
        


# In[ ]:




