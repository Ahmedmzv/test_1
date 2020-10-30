# list_ = list()           чтобы создать пустой список
# list_ = []
# list_ = list("hello")
# # print(type(list_))         чтобы разбить по одной букве
# print(list_)


# a = "hello"
# b = a.replace("l","k")        заменяет одну букву на другую
# print(b)


# a = [1,2,3,4]
# a.pop()
# print(a)

# a = [1,2,3,4], [1,3,4], 
# print(len(a))       функция len показывает колличество списков в скобках

# a = [1,2,3,4, [1,3,4]]
# a[1] = 5
# a.insert(0,0)
# print(a)


# a = [1,2,3,4,5,6]
# a = a[2::2]
# print(a)


# a = [1,2,3,4,5,6]
# b = ["a","b"]
# c = a + b

# # a.extend(b)       добавляет в скобки букву если есть цифра
# print(a)


# a = [1,2,3,4,5,6,"a"]
# c = a[0]*3
# a = "hello"*2
# print(a)



# # a = tuple([1,2,3])
# b = [1,2,3]
# a = tuple(b)

# c = (1,)
# print(type(c))
# print(a)


# a = ('a','b','c',1,2,False,None,[1,2], {'key': 'value'})
# # print(a.count('a'))
# # print(a.index([1,2]))

# del a
# print(a)

# def is_even(number):
#     return number % 2==0
#     def test_is_even():
#         assert is_even(2) == True
#         assert is_even(3) == False
#         assert_is_even(8) == True
#         assert_is_even(100) == True
#         assert_is_even(101) == False


# a = 2
# b = 3

# a,b = b,a

# print('a',a)
# print('b',b)

# a = 1,'a'
# print(type(a))


# a = (1,2,3)
# b,c,d = a
# print(a)
# print(b)                        распаковка обЬекта(1,2,3 = bcd)
# print(c)
# print(d)



# a = (1,2,3,4,5,6,7)
# b,*c,d = a
# print(b)
# print(c)
# print(d)
