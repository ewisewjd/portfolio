#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def binarySearch(data, left, right, q):
    if left > right:
        return left  

    mid = (left + right) // 2
    if data[mid] == q:
        return mid
    elif data[mid] > q:
        return binarySearch(data, left, mid - 1, q)  
    else:
        return binarySearch(data, mid + 1, right, q)  

def choose_value(data, q):
   
    idx = binarySearch(data, 0, len(data) - 1, q)
    
    
    answers = []
    
    # 좌측 값
    if idx - 1 >= 0:
        answers.append(data[idx - 1])
    
    # 우측 값
    if idx < len(data):
        answers.append(data[idx])
    
    choose = min(answers, key=lambda x: (abs(x - q), x))
    return choose

t = int(input())

for _ in range(t):
    # 각 테스트 케이스 마다 두줄을 입력받는다. 1. 띄어쓰기로 구분된 숫자 리스트 2. 찾고자하는 숫자리스트
    data = list(map(int, input().split()))
    query = list(map(int, input().split()))
    
    answer = [choose_value(data, q) for q in query]
    print(*answer)

