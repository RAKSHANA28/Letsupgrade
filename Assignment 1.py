>>> list=[1234, "hello", 1.732, "bye"]
>>> list
[1234, 'hello', 1.732, 'bye']>>> list.append("hai")
>>> list
[1234, 'hello', 1.732, 'bye', 'hai']
>>> list[0]
1234
>>> list[4]
'hai'
>>> list.count
<built-in method count of list object at 0x00000230906F4808>
>>> list1=list.count
>>> list1
<built-in method count of list object at 0x00000230906F4808>
>>> list.pop(2)
1.732
>>> del list[2]
>>> list
[1234, 'hello', 'hai']
>>> list.count('h')
0
>>> count = list.count('i')
>>> print("the count is",count)
the count is 0
>>> count = vowels.count('a')
>>> count
1
>>> list=[1, 5, 3, 9, 18]
>>> list
[1, 5, 3, 9, 18]
>>> list.sort
<built-in method sort of list object at 0x0000023090DA6688>
>>> list.sort()
>>> list
[1, 3, 5, 9, 18]
>>> list.reverse()
>>> list
[18, 9, 5, 3, 1]
>>> tuple=("hey", "hi", 12345, 2814)
>>> tuple
('hey', 'hi', 12345, 2814)
>>> x= tuple.count(2814)
>>> x
1
>>> tuple=(1,2,2,3,4,4,55,5,5,5,6)
>>> x= tuple.count(5)
>>> tuple.index(5)
7
>>> set={54321, 1234}
>>> set
{54321, 1234}
>>> set={1234, 5432, "apple", "orange"}
>>> set
{5432, 'orange', 1234, 'apple'}
>>> set.add('banana')
>>> set
{'orange', 'banana', 'apple', 1234, 5432}
3
>>> set.update(["papa"])
>>> set
{'orange', 'banana', 'apple', 'papa', 1234, 5432}
>>> set.update("dates")
>>> set
{'orange', 'banana', 'apple', 'd', 'e', 'papa', 'a', 1234, 's', 5432, 't'}
>>> set.update(["dates"])
>>> set
{'orange', 'banana', 'dates', 'apple', 'd', 'e', 'papa', 'a', 1234, 's', 5432, 't'}
>>> set.remove("dates")
>>> set
{'orange', 'banana', 'apple', 'd', 'e', 'papa', 'a', 1234, 's', 5432, 't'}
>>> x=len(set)
>>> x
11
>>> set.pop()
'orange'
>>> set.clear()
>>> set
set()
>>> dict ={"name": "rama" , "age": "25" ,"email id": "ramaseetha@gmail.com","ph no": "1234567"}
>>> dict
{'name': 'rama', 'age': '25', 'email id': 'ramaseetha@gmail.com', 'ph no': '1234567'}
>>> dict={"name": "rama", "age": "25" ,"email id": "ramaseetha@gmail.com","ph no": "1234567"}
>>> dict
{'name': 'rama', 'age': '25', 'email id': 'ramaseetha@gmail.com', 'ph no': '1234567'}
>>> dict.popitem()
('ph no', '1234567')
>>> dict.pop("age")
'25'
>>> dict.update({"age" : "15"})
>>> dict
{'name': 'rama', 'email id': 'ramaseetha@gmail.com', 'age': '15'}
>>> dict.values
<built-in method values of dict object at 0x0000023090E00AE8>
>>> dict.values()
dict_values(['rama', 'ramaseetha@gmail.com', '15'])
>>> dict.clear()
>>> dict
{}
>>> x= "monkey"
>>> print(x)
monkey
>>> str.capitalize(x)
'Monkey'
>>> str.encode(x)
b'monkey'
>>> txt= " hey, welcome to the world"
>>> x= txt.index("welcome")
>>> print(x)
6
>>> x=txt.find("to")
>>> print(x)
14
>>> str.casefold("MONKEY")
'monkey'
