a=int(input('������� �����'))
if a == 0:
    print(a)
while a > 0:
    b = a % 10
    a= a // 10
    print(b)