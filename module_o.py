#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np                       
number = np.random.randint(1,101)   # загадали число
print ("Загадано число от 1 до 100")

def game_core_v2(number):
    lower=0
    upper=101
    count = 0
    while (lower+upper)//2 != number:
        count+=1
        mid = (lower+upper)//2
        if  number<mid:
            upper=mid
        elif number>mid:
            lower=mid
        elif number==mid:
            break
            
    return(count) # выход из цикла, если угадали
game_core_v2(number)       


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core_v2)            


# In[ ]:




