from random import *

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if num > 0 and num < 101:
            return True
        else:
            return False
    else:
        return False
   
a = randint(1,100)
print('Добро пожаловать в числовую угадайку! Введите число: ')

while True:
    q = input()
    if not is_valid(q):
        print('Некорректное число, введите число от 1 до 100: ')
        continue
    q = int(q)
    if q > a:
        print('Слишком много, попробуйте еще раз')
    elif q < a:
        print('Слишком мало, попробуйте еще раз')
    else: 
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

