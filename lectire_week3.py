# names = ("nurbek","atay","ermek","nariza","bakyt")
# capitalized_names = []
# for name in names:
#     capitalized_names.append(name.capitalize())

# print(capitalized_names)

#                                  для того чтобы имена с маленькой буквы сделать с больших букв

# names = ["nurbek","atay","ermek","nariza","bakyt"]
# capitalized_names = [name.capitalize() for name in names]
# print(capitalized_names)


# nums = range(10)
# print("Nums = ",nums)
# new [item*3 for item in items]
# squared_nums = ["num" + str(num) for num in nums]
# print(list(nums))
# print("squared_nums=",squared_nums)


# users = ["Bakyt","Amantay","Atabek","The Best","Syimyk"]
# users_that_know_iterator = [user for user in users if user == "Amantay"]
# print(users_that_know_iterator)


# чтобы получить только положительные числа

# nums = [1,2,3,4,-3,-6,0,-1,4,8,-3]
# positive_nums = [num for num in nums if num >= 0 ]                  
# print(positive_nums)


#чтобы получить нечетные чиисла

# nums = [1,2,3,4,5,6,0,1,4,8,3]
# odd_nums = [num for num in nums if num % 2 != 0 and num > 0]
# print(odd_nums)



# nums = range(100)
# nums = [num for num in nums if num%5 == 0 and num %3 == 0]
# print(nums)


#табуляция по порядку
# for num in range(1,10):
#     print(end='\n')
#     for num2 in range(1,10):
#         print(num * num2,end = '\t')


# for num in range(1,10):
#     rint(end = '\n')
#     for num2 in range(1,10):
#         print(num * num2,end='\t')

# numss = [num * num2 for num2 in range(1,10) for num in range(1,10)]
# print(numss)



# по порядку вытаскивает(евен\одд)
# nums = ['even' if num % 2==0 else 'odd' for num in range(20)]
# print(nums)

