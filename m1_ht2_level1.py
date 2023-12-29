num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))
if (num1 == num2) + (num1 == num3) + (num2 == num3) == 3:
    print(3)
elif (num1 == num2) + (num1 == num3) + (num2 == num3) == 1:
    print(2)
else:
    print(0)