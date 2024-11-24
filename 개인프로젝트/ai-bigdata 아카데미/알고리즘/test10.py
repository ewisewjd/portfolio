#!/usr/bin/env python
# coding: utf-8

# In[4]:


# t=int(input())
# for _ in range(t):
#     insert_coin=int(input())
#     count_coin=0
#     count_coin+=insert_coin//50000
#     count_coin+=(insert_coin%50000)//10000
#     count_coin+=((insert_coin%50000)%10000)//5000
#     count_coin+=(((insert_coin%50000)%10000)%5000)//1000
#     count_coin+=((((insert_coin%50000)%10000)%5000)%1000)//500
#     count_coin+=(((((insert_coin%50000)%10000)%5000)%1000)%500)//100
#     print(count_coin)


# In[10]:


t=int(input())
for _ in range(t):
    n=int(input())
    coins=[50000,10000,5000,1000,500,100]
    coinnum=0
    for coin in coins:
        coinnum+=n//coin
        n%=coin
    print(coinnum)
   


# In[ ]:




