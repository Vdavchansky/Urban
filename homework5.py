immutable_var = 1,2,3,"Alex",True,1.0
print(immutable_var)
# immutable_var = 1,2,3,4,5,6,7,8
mutable_list = [0,1,2,3,"четыре",5,True,7.0]
print(mutable_list)
mutable_list.remove(0)
mutable_list.remove("четыре")
mutable_list.remove(True)
mutable_list.append(8)
mutable_list.extend("91011")
print(mutable_list)
