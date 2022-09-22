import matplotlib.pyplot as plt

age = ['0-9', '10-19', '20-29', '30-39',
       '40-49', '50-59', '60-69', '70-79', '> 80']
people_new_year = [444851 + 588347, 533786 + 464731, 445229 + 520539, 724861 + 781956, 689143 +
                   639636, 615008 + 645018, 685683 + 540113, 407613 + 190090, 338920]

people_average_year = [535311 + 559328, 501231 + 455275, 453187 + 627098, 783689 + 744104, 668849 +
                       639488, 628396 + 711447, 672803 + 514700, 329546 + 233908, 361398]


def answer(choose):
    if choose == 1:
        plt.bar(age, people_new_year)
        plt.xlabel('Возраст')
        plt.ylabel('Численность населения')
        plt.title('Численность населения на начало периода (оба пола)')
        plt.show()
        return 1

    if choose == 2:
        plt.bar(age, people_average_year)
        plt.xlabel('Возраст')
        plt.ylabel('Численность населения')
        plt.title('Среднегодовая численность населения')
        plt.show()
        return 1

    if choose == 3:
        return 0

    if choose not in (1, 2, 3):
        raise Exception('Неправильно')


def start():
    flag = True
    while flag:
        choose = int(input(
            '****************************************************************\nВыберите график:'
            '\n1. Численность населения на начало периода 2022 года. '
            '\n2. Среднегодовая численность населения'
            '\n3. Выход'
            '\nВаш выбор: '))
        flag = answer(choose)


if __name__ == '__main__':
    start()
