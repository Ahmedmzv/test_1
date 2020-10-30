# x = int (input("введите число:"))
# y = int (input("введите число:"))

# try:
#     res = x/y
# except ZeroDivisionError:
#     print("Exception:к сожалению на ноль делить нельзя")
#     res = 0
# print(res)


# a = input("введите ппервую цифру:")
# b = input("введите вторую цифру:")
# try:
#     res = int(a) + int(b)
#     print(res)
# except ValueError:
#     print("вы задали неправильный параметр,инпут ожидает число!")


# dict_ = {"key1":"value1","key2":"value2"}
# try:
#     dict_["key3"]
# except KeyError:
#     raise Exception("Вы задали неправильный параметр,инпут ожидает число!")



# int_ = input("введите номер:")
# try:
#     if int_.startswith('(') and int_.endswith(')'):
#         print("Hello")
#     elif int_ !=int_.startswith('('):
#         raise TypeError("Данная программа принимает только intger!")
# finally:
#     print('Bye')





# lists = [1,2,3,4]
# length = len(lists) - 0
# try:
#     lists[5]
# except IndexError:
#     raise Exception(f'{length} - last index')