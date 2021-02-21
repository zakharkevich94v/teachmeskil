num1 = input("Введите число: ")
num2 = len(num1)//2
num3 = num1[num2]
print(num3)
if num3 == num1[0]:
    print(num1[1:-1:])
