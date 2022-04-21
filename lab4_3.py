dict_eng = {'white': 'белый', 'yellow': 'желтый', 'red': 'красный', 'green': 'зелёный', 'blue': 'синий',
            'table': 'стол', 'window': 'окно', 'pen': 'ручка', 'bed': 'кровать', 'pencil': 'карандаш',
            'turkey': 'индюк', 'cat': 'кошка', 'dog': 'собака', 'cow': 'корова', 'brother': 'брат',
            'phone': 'телефон'}

my_list = []

while True:
    s = input('Введите слово\n\t')
    print(dict_eng[s])
    my_list.append(dict_eng[s])
    b = int(input('Хотите повторить: 1:да , 2:нет '))
    if b == 1:
        continue
    else:
        break

my_list.sort()
print(my_list)

#new_list = sorted(dict_eng.items(), key=lambda x: x[1])
#sort_values = dict(new_list)
#print(sort_values)
