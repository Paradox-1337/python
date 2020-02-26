my_list = [7, 5, 3, 3, 2]
print("Рейтинг", my_list)
user_number = int(input("Введите число: "))
for element in range(len(my_list)):
    if my_list[element] == user_number:
        my_list.insert(element + 1, user_number)
        break
    elif my_list[0] < user_number:
        my_list.insert(0, user_number)
    elif my_list[-1] > user_number:
        my_list.append(user_number)
print("текущий список", my_list)
