# class Employee:
#
#     def srj(self):
#         my_dict = {"sp": "surajpatil", "ps": "priya suraj", 1: "int value", True: "str value"}
#
#         my_dict.update({True: "NEW STR VALUE"})
#
#         return ((my_dict))
#
#
#
# object1 = Employee()
# print(object1.srj())
#
# my_str = "sur$aj@a"
#
# special_char = ["$","@"]
#
# new_str = ""
#
# new_dict = {}
#
# for i in my_str:
#     if i in special_char:
#         my_ind= my_str.index(i)
#         new_dict[my_ind] = i
#
#     else:
#         new_str += i
#
# rev_list = new_str[::-1]
# new_list = list(rev_list)
#
# for k,v in new_dict.items():
#     new_list.insert(k,v)
# print(new_list)
#
# a = "".join(new_list)
# print(a)




def decor(func):
    def inner():
        sp = func()
        return sp.upper()
    return inner

@decor
def srj():
    return ("suraj")

print(srj())




# def decor(func):
#     def inner():
#         sp=func()
#         return sp.upper()
#     return inner
#
#
# @decor
# def srj():
#     return ("suraj")
#
# print(srj())





















































