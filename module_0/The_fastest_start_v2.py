# coding: utf-8

import numpy as np

def game_core_v4(number):
    
    # Функция принимает загаданное число и возвращает число попыток угадывания (в среднем за 5.8 попыток)
    # Алгоритм перебора заменен на алгоритм половинного деления (разновидность метода последовательных приближений), 
    # границы множежства каждый раз "сужаются" в 2 раза пока одна из границ не "встанет" на угадываемое число 
   
    
    count = 1              # счетчик попыток
    high_predict = 100     # начальная верхняя граница
    low_predict = 0        # начальная нижняя граница
    predict = 50           # начальное предсказание (первая попытка, счетчик равен 1)
    
    while number != predict:
        count+=1
        
        if number > predict:            # если в верхней половине множества, сдвигаем нижнюю границу "вверх"
            low_predict = predict       
            predict = int(np.around( (low_predict+high_predict)/2 ))

        elif number < predict:          # если в нижней половине множества, сдвигаем верхнюю границу "вниз"
            high_predict = predict      
            predict = int(np.around( (low_predict+high_predict)/2 ))

       # выход из цикла, если угадали

    return(count) 
        
def score_game(game_core):
    
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000)) # заполняем 1000 случайных чисел
    
    for number in random_array:
        count_ls.append(game_core(number))    # для каждого случайного числа записываем каличество попыток
        
      
    score = np.mean(count_ls)                 # считаем среднее каличество попыток для 1000 чисел  
        
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

score_game(game_core_v4)



