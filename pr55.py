list1 = ['apple', 'banana', 'orange']
list2 = [1, 2, 3]

dictionary = dict(zip(list1, list2))

print(dictionary)
14.
dic1 = {
  2:2,
  1:4
}
dic2 = dict(sorted(dic1.items()))
print(dic2)
15.
my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

max_value = max(my_dict.values())
min_value = min(my_dict.values())

print("Maximum value:", max_value)
print("Minimum value:", min_value)
16.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Person("John", 25, "Male")

dictionary = vars(person)

print(dictionary)