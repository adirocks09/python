print("\n*************Hello World************************\n");

name = "Aditya";

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

if (department is None) :
  print ("Department Not Found");

if(salary is not None) :
  print ("Salary is Available");