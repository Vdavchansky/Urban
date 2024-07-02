my_dict = {"Alex": 2002, "Katrin": 1994, "Viktor": 1988}
print(my_dict)
print(my_dict["Alex"])
print(my_dict.get("Natasha"))
my_dict.update({"Danil": 2005,
                "Andrew": 2002})
print(my_dict)
a = my_dict.pop("Viktor")
print(my_dict)
print(a)

my_set = {1,2,3,4,5,1,2,3,4}
my_set.add(6)
my_set.add(7)
my_set.remove(1)
print(my_set)