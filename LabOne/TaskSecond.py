from tkinter import *


def clicked():
    number = txt.get()
    c = Checker(number)
    c.str_to_type()

    is_int = Label(window, text=str(c.is_int), fg='#0f0' if c.is_int else '#f00')
    is_int.grid(column=1, row=1)

    is_float = Label(window, text=str(c.is_float), fg='#0f0' if c.is_float else '#f00')
    is_float.grid(column=1, row=2)

    is_fib = Label(window, text=str(c.is_fibonacci()), fg='#0f0' if c.is_fibonacci() else '#f00')
    is_fib.grid(column=1, row=3)

    is_complex = Label(window, text=str(c.is_complex), fg='#0f0' if c.is_complex else '#f00')
    is_complex.grid(column=1, row=4)

    is_prime = Label(window, text=str(c.is_prime()), fg='#0f0' if c.is_prime() else '#f00')
    is_prime.grid(column=1, row=5)


def fibonacci_of(n):

    if n in (0, 1):
        return n

    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


def fibonacci_list(n) -> list:
    return [fibonacci_of(i + 1) for i in range(n)]


class Checker:
    num = 0
    is_int = False
    is_float = False
    is_complex = False

    def __init__(self, num):
        self.num = num

    def str_to_type(self) -> None:

        self.num = ''.join(self.num.split())

        try:
            self.num = int(self.num)
            self.is_int = True
        except ValueError:

            try:
                self.num = float(self.num)
                self.is_float = True
            except ValueError:

                try:

                    if 'j' in self.num and ('+' in self.num or '-' in self.num):

                        self.num = complex(self.num)
                        self.is_complex = True

                except ValueError:
                    pass

    def is_prime(self) -> bool:

        if not isinstance(self.num, int):
            return False
        else:
            if self.num < 2:
                return False
            else:
                for i in range(2, self.num):
                    if (self.num % i) == 0:
                        return False
                return True

    def is_fibonacci(self) -> bool:

        if not isinstance(self.num, int):
            return False
        else:

            if self.num > 0:

                fib_lst = fibonacci_list(30)

                for f in fib_lst:
                    if self.num == f:
                        return True
                    if f > self.num:
                        return False
            else:
                return False


if __name__ == '__main__':
    window = Tk()
    window.title("Number checker")
    window.geometry('300x150')

    lbl = Label(window, text="Введите число:")
    lbl.grid(column=0, row=0)

    int_lbl = Label(window, text='Целочисленное:')
    int_lbl.grid(column=0, row=1)

    float_lbl = Label(window, text='Вещественное:')
    float_lbl.grid(column=0, row=2)

    fib_lbl = Label(window, text='Число Фибоначчи:')
    fib_lbl.grid(column=0, row=3)

    complex_lbl = Label(window, text='Комплексное:')
    complex_lbl.grid(column=0, row=4)

    prime_lbl = Label(window, text='Простое число:')
    prime_lbl.grid(column=0, row=5)

    btn = Button(window, text="Проверить число", command=clicked)
    btn.grid(column=2, row=0)

    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)

    window.mainloop()
