import numpy as np

def game_core_v3(number):
    '''Задаем диапазон, устанвливаем число, являющееся серединой диапазона. 
       Затем выбираем нужную половину диапазона и повторяем. 
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    bottom = 1
    top = 100
    predict = (bottom + top)//2
    while number != predict:
        count +=1
        if number > predict:
            bottom = predict + 1  # увеличиваем ниржнюю границу дипазона, если число больше установлденного
            predict = (bottom + top)//2
        else:
            top = predict - 1  # уменьшаем верхнюю границу дипазона, если число меньше установлденного
            predict = (bottom + top)//2
    return (count)        
     
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

score_game(game_core_v3)

