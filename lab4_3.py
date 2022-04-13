dict_eng = {'white': 'белый', 'yellow': 'желтый', 'red': 'красный', 'green': 'зелёный', 'blue': 'синий',
'table': 'стол', 'window': 'окно', 'pen': 'ручка', 'bed': 'кровать', 'pencil': 'карандаш',
'turkey': 'индюк', 'cat': 'кошка', 'dog': 'собака', 'cow': 'корова', 'brother': 'брат'}
while True:
    s = input()
    print(dict_eng[s])
    b = int(input('Хотите повторить: 1:да , 2:нет '))
    if b == 1:
        continue
    else:
        break