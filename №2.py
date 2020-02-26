user_input = input("Введите элементы , для создания списка (через пробел): ")
user_list = user_input.split()
start_step = 0
for element in range(int(len(user_list) / 2)):
    user_list[start_step], user_list[start_step + 1] = user_list[start_step + 1], user_list[start_step]
    start_step += 2

print(user_list)