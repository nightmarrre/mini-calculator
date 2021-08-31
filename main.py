import time
from operations import addition as add
from operations import subtraction as sub
from operations import multiplication as multi
from operations import division as div
from operations import square_root as sqrt
from operations import percent as per


def main():
    while True:
        print('Choose the operation you want to perform: ')
        print('Enter 1: Addition')
        print('Enter 2: Subtraction')
        print('Enter 3: Multiplication')
        print('Enter 4: Division')
        print('Enter 5: Square Root')
        print('Enter 6: Percent')
        print('Enter 7: Exit')
        choose = int(input('Enter your choice: '))

        if choose == 1:
            num_1 = int(input('Enter the first number: '))
            num_2 = int(input('Enter the second number: '))
            print(f'{num_1} + {num_2} = {add.addition(num_1, num_2)}')
            time.sleep(3)

        elif choose == 2:
            num_1 = int(input('Enter the first number: '))
            num_2 = int(input('Enter the second number: '))
            print(f'{num_1} - {num_2} = {sub.subtraction(num_1, num_2)}')
            time.sleep(3)

        elif choose == 3:
            num_1 = int(input('Enter the first number: '))
            num_2 = int(input('Enter the second number: '))
            print(f'{num_1} * {num_2} = {multi.multiplication(num_1, num_2)}')
            time.sleep(3)

        elif choose == 4:
            num_1 = int(input('Enter the first number: '))
            num_2 = int(input('Enter the second number: '))
            print(f'{num_1} / {num_2} = {div.division(num_1, num_2)}')
            time.sleep(3)

        elif choose == 5:
            num = int(input('Enter the number: '))
            print(f'Square root {num} = {sqrt.square_root(num)}')
            time.sleep(3)

        elif choose == 6:
            num = int(input('Enter the number: '))
            print(f'{num}% = {per.percent(num)}')
            time.sleep(3)

        elif choose == 7:
            break


main()
