# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!
# Создайте список списков населения перечисленных городов
# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек
# Создайте список списков населения перечисленных городов
# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек
# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек


cities = [
    ["Moscow", 12535000] , 
    ["Nizhny Novgorod", 1233000],
    ["Samara", 1136000],
    ["Sochi", 433000],
    ["Ekb", 1493000]
]
 
print(f'Население в городе', cities[1][0], ' - ', cities[1][1])

summ = cities[0][1] + cities[1][1] + cities[2][1] + cities[3][1]+ cities[4][1]
print(f'Итого размер населения: ',  summ)


