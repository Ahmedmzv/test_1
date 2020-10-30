# a = set()                                  создает пустую строку 
# print(type(a))

# a = set("string")                 сет неуппорядочный
# print(a)

# a = set([1,2,3,1,2,3])                   избавляет от дубликатов не только чисел,но и строк
# print(a)

# a = {"a","b","c"}
# a.add("d")           добавляет только один элемент
# a.update({"f","l"}),({"m","n"})      добавляет несколько элементов#
# a.remove("c")    удаляет
# a.discard("d")      удаляет без ошибок
# b = a.pop()
# print(a)
# print(b)

# a = {"a","b","c",""}                      
# if "d" not in a:
#     a.add("d")                    добавляет адд удаляет римув
# print(a)
# lenght = len(a)                        возвращает коллво элементов
# print(lenght)


krujok1 = {"Masha","Sasha","Nikita","Syimuk","Aipery"}
krujok2 = {"Syimuk","Masha"}
krujok3 = {"Mirbek","Dastan","Nikita"}
b = dancing.difference(singing)
x = krujok1.difference(krujok2,krujok3)
print(x)
print(b)
# x = dancing.intersection(singing)
# x = krujok3.intersection(krujok1,krujok2)
# x = krujok1 & krujok2 & krujok3
# print(x)
# c = singing.symmetric_difference(dancing)
# c = krujok1 ^ krujok2 ^ krujok3
# print(c)                                           
# d = singing.union(dancing)
# print(d)
# print(dancing.issubset(singing))
# print(singing.issubset(dancing))


# "-" - разность
# "^" - симетричная разность
# "&" - пересечение
# "|" - обЬединение


# frozen_krujok1 = frozenset(krujok1)
# print(type(frozen_krujok1))
