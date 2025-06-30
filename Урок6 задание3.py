a = int(input())#инвестиции
b = int(input())#Иван
c = int(input())#Майкл
if (a < b) and (a < c):
    print(2)
elif (a < b) or (a < c) or (a < (b + c)):
    print(1)
else:
    print(0)