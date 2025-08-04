my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list_recursive(lst):
    if not lst:
        print("Конец списка")
        return
    print(lst[0])            
    print_list_recursive(lst[1:])  

print_list_recursive(my_list)