print("\n*************Hello World************************\n");

name = input ("Enter your name : ")  # takes input from user

age = 34;

salary = 100.5;

is_boy = True;

print (name, age, salary, is_boy);

print (type(name), type(age), type(salary), type(is_boy));

description = f"My name is {name}. Age is {age} . My salary is {salary}.";

print(description);

# Typecasting
print (name + " " + str(age)); 

print (age + salary);

print("\n********************************\n");

print (isinstance(age, int));
print (isinstance(age, float));

print (isinstance(name, str));

print (isinstance(salary, float));

print(isinstance(is_boy, bool));

print("\n********************************\n");

#dynamically_typed : data type can be changed at any point of time

is_boy = "yes";
print(is_boy);
print(isinstance(is_boy, str));

print("\n********************************\n");

# list : mutable collection  (can contain different datatype)
data_list = [10, "hello", 10.5, True]

for index, value in enumerate(data_list) :
  print (index, value);

print("\n********************************\n");

# tuple : immutable collection  (can contain different datatype)
data_tuple = (10, "hello", 10.5, True);

for index, value in enumerate(data_tuple) :
  print (index, value);

print("\n********************************\n");

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

# tuple operations
tuple_add = tuple1 + tuple2
print(tuple_add)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
tuple_multiply = fruits * 2

print(tuple_multiply)

# tuple destructurization
(x1, x2, x3) = tuple1
print (x1, x2, x3)

(f1, *f2, f3) = fruits
print (f1, f2, f3)

# Exception is thrown during destructurization if number of lhs elements and rhs elements are not same
#(t1, t2, t3) = fruits
#print (t1, t2, t3)

# set : unique values 
data_set = {10, 20, 30, 20}

for index, value in enumerate(data_set) :
  print (index, value);

print("\n********************************\n");

# operators : & , |

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)  # intersection → {2, 3}
print(a | b)  # union        → {1, 2, 3, 4}

print("\n********************************\n");

# logical operators : and, or, not

res_1 = (2 > 0) and (3 > 1);
res_2 = (2 > 0) or (3 < 1);
res_3 = not (2 > 0) ;

print (res_1, res_2, res_3);

# null check

department = None;

print(department);

print(type(department));

if (department is None) :
  print ("Department Not Found");

if(salary is not None) :
  print ("Salary is Available");

list_1 = [1,2,3];

list_2 = [1,2,3];

list_3 = list_1;

print (list_1 == list_2)  # Compares data 
print (list_1 == list_3)  # Compares data

print (list_1 is list_2)  # Compares reference
print (list_1 is list_3)  # Compares reference


# Date Time Manipulation

print("\n**************Date & Time******************\n");

# import statements can be declared just before using it at any point in the file but its recommended to use it at the beginning of the file

from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("GMT"))

# Extract individual fields

print(f"Date & Time : {now} :: {type(now)}")
print(f"Year: {now.year} :: {type(now.year)}")
print(f"Month: {now.month} :: {type(now.month)}")
print(f"Day: {now.day} :: {type(now.day)}")
print(f"Hour: {now.hour} :: {type(now.hour)}")
print(f"Minute: {now.minute} :: {type(now.minute)}")
print(f"Second: {now.second} :: {type(now.second)}")
print(f"Microsecond: {now.microsecond} :: {type(now.microsecond)}")
print(f"Timezone Info: {now.tzinfo} :: {type(now.tzinfo)}")

# formatting date into String

formatted_date = now.strftime("%d-%m-%Y %H::%M::%S %Z") 
print (formatted_date)
