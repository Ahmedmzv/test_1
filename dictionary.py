# student = {"name":"Ahmed","surname":"Mazunov","age":23}
# studenty = {}
# print(type(studenty))
# studenty = dict((("winter",1), ("spring",  2),("fall", 3)))
# print(student)


# student['name']='Ahmed'
# print(student['name'])
# # del student['name']
# print(student)
# surname = student.get('surname')            
# name = student['name']
# print(surname)
# print(name)


# student = {
#     'name':'Ahmed',
#     'surname':'Mazunov',
#     'age':23,
#     'languages':['englih','russian','kyrgyz'],
#     'smokes': False,
#     'other_dict':{1:'one',2:'two'},
#     True: "True goi",
#     None: 'None goi',
#     (1,2,3): 'eto tuple',
#     'name':'Moi name'
#     }
# print(student['name'])
# print(student['other_dict'][2])


# my_tuple =(("one",1),("two",2),("there",3))
# dict_ = dict()
# print(dict_)


# days = [1,2,3]
# days_names = ["mon","thus","wed"]
# dict_days =  (dict)zip(days,days_names)
# print(dict_days)


# student.clear()          полностью очищает


# new_student = student.copy()                      копирует
# print(new_student)                              

# print(student.items())                  делает из элементтов словаря список


# for item in student.items():
#     print(items)                           соддержит (1) элемент


# print(student.values())
# for item in student.keys():
#     print(item)


# new_item = student.pop("name","Ahmed")
# print(new_item)
# print(student)


# new_item = student.popitem()
# print(new_item)
# print(student)


# student.setdefault(10,"DEFAULT")
# print(student)

# student.update[(('black',6),(white,8)])                           принимает или словарь ли список
# print(student)

# student.update({"key1":,"key2": 2})
# print(student)

# student = dict.fromkeys([1,2,3],"Makers")
# print(student)