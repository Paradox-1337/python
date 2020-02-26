user_str = input("Введите строку (через пробел): ")
my_list = user_str.split()
print(my_list)
start_step = 1
for element in my_list:
    if len(element) > 10:
        print(element[0:11], start_step, "строка")
        start_step += 1
    else:
        print(element, start_step, "строка")
        start_step += 1
print("На этом все)")