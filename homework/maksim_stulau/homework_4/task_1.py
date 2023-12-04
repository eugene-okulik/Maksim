my_dict = {"tuple": (1, 'text', 3, 4, 5),
           "list": ["start", 1, 33.3, True, [], {7, "text"}],
           "dict": {"name": "Maksim", "age": 43, "job": "QA", "maried": True, 2: 3},
           "set": {6, 7, 'text', 9, 10}}

print(my_dict)

last_value = my_dict["tuple"]
# print(last_value)
# print(last_value[-1])

add_del_list = my_dict["list"]
# print(add_del_list)
del_list = add_del_list.pop(2)
add_del_list.append(33)
# print(add_del_list)

new_dict = my_dict["dict"]
# print(new_dict)
new_dict["i am a tuple"] = 1
new_dict.pop("age")
# print(new_dict)

new_set = my_dict["set"]
# print(new_set)
new_set.remove(6)
new_set.add(333)
# print(new_set)

print(my_dict)
