import sys
age = 32 #integer variable
name = "Kiran Kapikad" #string variable
height = 5.7 #float variable
is_student = False #boolean variable
complex_number = 3 + 4j #complex variable
bytes_variable = b"Hello" #bytes variable
byte_array_variable = bytearray(b"Hello") #bytearray variable
none_variable = None #None variable
list_variable = [1, 2, 3, 4, 5] #list variable
tuple_variable = (1, 2, 3, 4, 5) #tuple variable
set_variable = {1, 2, 3, 4, 5} #set variable
frozenset_variable = frozenset([1, 2, 3, 4, 5]) #frozenset variable
dict_variable = {"name": "Kiran", "age": 32, "height": 5.7} #dictionary variable
print("Name:", name) #print the value of name
print("Age:", age) #print the value of age
print("Height:", height) #print the value of height
print("Is Student:", is_student)  #print the value of is_student
print("Complex Number:", complex_number)  #print the value of complex_number
print("Bytes Variable:", bytes_variable)  #print the value of bytes_variable
print("Byte Array Variable:", byte_array_variable)  #print the value of byte_array_variable
print("None Variable:", none_variable)  #print the value of none_variable   
print("List Variable:", list_variable)  #print the value of list_variable
print("Tuple Variable:", tuple_variable)  #print the value of tuple_variable
print("Set Variable:", set_variable)  #print the value of set_variable
print("Frozen Set Variable:", frozenset_variable)  #print the value of frozenset_variable
print("Dictionary Variable:", dict_variable)  #print the value of dict_variable
print("---------------Size------------------")
# print memory size of each variable
print("Integer : ",sys.getsizeof(age), "bytes") #size of integer variable
print("String : ",sys.getsizeof(name), "bytes") #size of string variable
print("Float : ",sys.getsizeof(height), "bytes") #size of float variable
print("Boolean : ",sys.getsizeof(is_student), "bytes") #size of boolean variable
print("Complex : ",sys.getsizeof(complex_number), "bytes") #size of complex variable
print("Bytes : ",sys.getsizeof(bytes_variable), "bytes") #size of bytes variable
print("Bytearray : ",sys.getsizeof(byte_array_variable), "bytes") #size of bytearray variable
print("None : ",sys.getsizeof(none_variable), "bytes") #size of None variable
print("List : ",sys.getsizeof(list_variable), "bytes") #size of list variable
print("Tuple : ",sys.getsizeof(tuple_variable), "bytes") #size of tuple variable
print("Set : ",sys.getsizeof(set_variable), "bytes") #size of set variable
print("Frozen Set : ",sys.getsizeof(frozenset_variable), "bytes") #size of frozenset variable
print("Dictionary : ",sys.getsizeof(dict_variable), "bytes") #size of dictionary variable