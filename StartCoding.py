# Hello world
print("hello world")

# 变量可以包含字母、数字和下划线
msg_from_computer = "Hello"  # String
another_msg = 'Hello in single quote'  # also a String

print(msg_from_computer + " World..!")

# Type will return the data type
print(type(msg_from_computer))  # <type 'str'>

# 数字与字符串拼接
count = 5
print("I need " + str(count) + " chocolates")

bool("")  # false

numbers = ["one", "two", "three"]

numbers[-1]  # = three. If we pass negative value Python whill start from th end
numbers[-2]  # two
len(numbers)  # 3
numbers.append("four")  # add value to the last
numbers.insert(1, "wrong_one")  # insert value before pos 1
del numbers[1]  # delete the value at the pos 1
popped_element = numbers.pop()  # remove the last element
print(popped_element)  # four
print(numbers)  # ['one', 'two', 'three']
numbers.reverse()
print(numbers)  # ['three', 'two', 'one']

numbers.remove("two")  # remove elements by value

# Sorting
alpha = ["z", "c", "a"]
alpha.sort()
print(alpha)  # ['a', 'c', 'z']

alpha.sort(reverse=True)
print(alpha)  # ['z', 'c', 'a']

print(sorted(alpha))  # ['a', 'c', 'z'] wont change origin variable
print(alpha)  # ['z', 'c', 'a']

# Slicing elements
alpha = ['a', 'b', 'c', 'd', 'e']
alpha[1:3]  # ['b', 'c']. The first element is the starting index. And Python stops in the item before the second index.
alpha[2:5]  # ['c', 'd', 'e']

alpha[:4]  # [ 'a', 'b', 'c', 'd'] In this case, the first index is not present, so Python startes from the beginning.

alpha[:3]  # ['a', 'b', 'c']

alpha[3:]  # ['d', 'e'] In this case, last index is not present. So it travels till the end of the list.

alpha[
:]  # ['a', 'b', 'c', 'd', 'e'] There is no starting or ending index. So you know what happens. And this helps you in copying the entire array. I think I don't have to explain that if you copy the array, then any changes in the original array won't affect the copied array.

another_alpha = alpha  # This is not copying the array. Any changes in alpha will affect another_alpha too.

num = (1)  # int
num = (1,)  # 元组和列表类似，但是不可变的
char = ('a',)
new_tuple = num + char
print(new_tuple)  # (1, 'a')

# 集合 元素不可重复
alpha = {'a', 'b', 'c', 'a', 'd'}
print(alpha)  # unordered & duplicates are removed {'a', 'c', 'd', 'b'}

# access items in set
for ele in alpha:
    print(ele)

alpha.add('s')  # add a single value
alpha.update(['a', 'x', 'z'])  # add mutiple values

print(alpha)  # {'s', 'z', 'x', 'a', 'c', 'd', 'b'}
alpha.remove('a')
alpha.discard(
    'a')  # It's safer to use discard than remove. Discard will never throw an error even if the element is not present in the set but remove will do.

# 字典 K-V
user = {'id': 1, 'name': 'John wick', 'email': 'sdfgag@666.com'}
user['id']  # 1
len(user)  # 3
user['age'] = 35

# get all the keys
keys = user.keys()
print(keys)  # dict_keys(['id', 'name', 'email', 'age'])

# get all the values
values = user.values()
print(values)  # dict_values([1, 'John wick', 'sdfgag@666.com', 35])

del user['age']  # delete a key

# if..else
a = 5
b = 10
if a == 5 and b == 10:
    print('a=5 and b=10')
elif a == 6:
    print('a is six')
else:
    print('a not know')

if not a == 5:
    print('a is not five')

if a == 5: print('a is five')

print('a is five') if a == 5 else print('a is not five')

# while
i = 0
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        break

# But if you are using break in the loop, then Python will break out of the entire loop and it won't execute else part.
i = 10
while i <= 15:
    print(i)
    i += 1
    if i == 13:
        break
else:
    print('Completed')

# Output
10
11
12

# for
range(3)  # This code generates a sequences from 0 to 2.
range(1, 4)  # This code generates a sequence from 1 to 3.
range(1, 8, 2)  # This code generates a sequence with 1, 3, 5, 7

for ele in range(3):  # Prints from 0 to 2.
    print(ele)

    dict = {'name': 'John wick'}

    # You can iterate through a dictionary. items() will return both keys and values. You can also use keys() and values() if needed.
    for key, value in dict.items():
        print(key + " is " + value)


# function
# keyword arguments. You can pass explicitly which parameter should be matched. In this way, you don't have to send the arguments in order just explicitly mention the parameter name.
def movie_info(title, director_name, ratings):
    print(title + " - " + director_name + " - " + ratings)


movie_info(ratings='9/10', director_name='David Fincher', title='Fight Club')


def languages(*names):
    print(names)  # ('Python', 'Ruby', 'JavaScript', 'Go'). This is a tuple.
    return 'You have mentioned ' + str(len(names)) + ' languages'


print(languages('Python', 'Ruby', 'JavaScript', 'Go'))  # You have mentioned 4 languages


# 关键字作为参数
def user_info(**info):
    print(info)  # {'id': 1, 'name': 'awst', 'fav_language': ['Rust', 'C++']}


user_info(id=1, name='awst', fav_language=['Rust', 'C++'])


def user_info(id, name, **info):
    print(info)  # {'fav_language': ['Rust', 'C++']}


user_info(1, 'awst', fav_language=['Rust', 'C++'])


# class
class Animal():
    # constructor
    def __int__(self, name):
        self.name = name

    def eat(self):
        print(self.name + ' eats')

    def sleep(self):
        print(self.name + " sleeps")


# initiating a class
dog = Animal('harry')
dog.eat()

print(dog.name)
dog.name = 'Rosie'  # modify attribute
print(dog.name)

class Dog(Animal):
    def __init__(self,name):
        self.name=name

    def eat(self):

        print('Dog eats')

dog1 = Dog('harry')
dog1.eat() # Dog eats
dog1.sleep() # Animal sleeps

# exceptions
try:
    some_error_raised
except:
    print('Exception handled')
else:
    print('No error raised.')
finally:
    print('this code will run whether has error or not')

def func(*args,**kwargs):
    print(args)
    print(kwargs)

func(1,3,3,x=9,y=10)