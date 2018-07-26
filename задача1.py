a=int(input('введите число'))
if a == 0:
    print(a)
while a > 0:
    b = a % 10
    a= a // 10
    print(b)