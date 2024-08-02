# Неизменяемые и изменяемые объекты. Кортежи
# task 1
immutable_var = 1.5, 2, True, 'apple'
print(type(immutable_var), immutable_var)

# task 2
# immutable_var[1] = 3
# print(immutable_var)  # элементы в кортеже - это как константы с которыми можно работать, но нельзя изменить.

# task 3
mutable_list = ["Вася", "Петя", "Коля", 3, 0.5]
print(type(mutable_list), mutable_list)
mutable_list[2] = 7.6
mutable_list.extend(["Olga"])
print(mutable_list)
