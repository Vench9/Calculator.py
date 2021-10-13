x=float(input("Введите значение x = "))
z=input("Введите оператор (+, -, /, *) ")
y=float(input("Введите значение y= "))
if z=="+":
    result=x+y
elif z=="-":
    result=x-y
elif z=="*":
    result=x*y
elif y!=0:
    if z== "/":
        result=x/y
elif y==0:
    result="Деление на 0!"
print("Результат вычеслений =", result)