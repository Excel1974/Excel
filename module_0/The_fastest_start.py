# coding: utf-8

import numpy as np

def game_core_v3(number):
    
    # Функция принимает загаданное число и возвращает число попыток (в среднем за 25 попыток)
    # Сначала устанавливаем не любое random число, а среднее число т.е. 50  
    # потом уменьшаем или увеличиваем его с шагом 1 в зависимости от того, больше оно или меньше нужного.
    
    
    count = 1        # счетчик попыток
    predict = 50     # угадываемое число, инициализация = 50
    
    while number != predict:     # перебираем последовательно "вверх" или "вниз" с шагом 1 
        count+=1
        
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
            
    return(count) # выход из цикла, если угадали
        
def score_game(game_core):
    
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000)) # заполняем 1000 случайных чисел
    
    for number in random_array:
        count_ls.append(game_core(number))   # для каждого случайного числа записываем каличество попыток 
    
    score = int(np.mean(count_ls))           # считаем среднее каличество попыток для 1000 чисел    
        
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)




