

# my_list = (1,2,3,4,5,34,5)
# print(type(my_list))
#
# temp = (i+2 for i in my_list)
# print(temp)

# my_str = "suraaajkkk"
#
# temp={i:my_str.count(i)for i in my_str}
# print(temp)
# my_str = "pypthon is a best langauage"
#
# temp={i:my_str.count(i)for i in my_str}
#
# sp=(min(temp,key=temp.get))
#
# temp1 = temp[sp]
# print(temp1)


# my_string = "gdjgf115"
# sp =0
# for i in my_string:
#     if i.isdigit():
#         sp=sp+int(i)
#
# print(sp)


my_str = "sura@j%pp"

special_char = ["@","%"]

new_str = ""

new_dict = {}


for i in my_str:
    if i in special_char:
        new_ind = my_str.index(i)
        new_dict[new_ind] = i
    else:
        new_str += i

rev_str = new_str[::-1]
new_list = list(rev_str)
print(new_list)

for k,v in new_dict.items():
    new_list.insert(k,v)

a = "".join(new_list)

print(a)



# my_list = [1,23,5,4,2,18,16,49]
#
# for i in range(len(my_list)-1):
#     print(i)
#     for j in range(len(my_list)-1):
#         if my_list[j]>my_list[j+1]:
#
#             my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
#
# print(my_list[-1])


# my_str = "sgdhgdjdgh"
# dup = []
# for i in my_str:
#     if my_str.count(i)>1:
#         dup.append(i)
#
# temp=(set(dup))
#
# a = "".join(temp)
# print(a)
#
# my_list = [1,23,4,5,2,6,78]
#
# for i in range(len(my_list)-1):
#     for j in range(len(my_list)-1):
#         if my_list[j]>my_list[j+1]:
#             my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
#
# print(my_list)
#
# object2 = EM






























