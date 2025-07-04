a = int(input())#инвестиции
b = int(input())#Иван
c = int(input())#Майкл
if (a <= b) and (a <= c):
    print(2)
elif (a <= b):
    print("Ivan")
elif (a <= c):
    print("Mike")
elif (a <= (b + c)):
    print(1)
else:
    print(0)