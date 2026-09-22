# no parameters
def get_name() :
  return "aditya";

# multiple parameters, void return type

def print_sum (a : int, b : int) -> None :
  print (a+b);

# multiple parameters, single return type
def get_sum(a : int, b : int) -> int :
  return a+b;

# multiple parameters, mixed return type
def get_sum_positive (a : int, b : int) -> int | str :
  if (a > 0 and b > 0 ) :
    return (a+b);
  else :
    return "Invalid Arguemnets";

# dictionary parameters, tuple return type
def get_user_data (user : dict) -> tuple [str, int, float] : 
  return user["name"], user["age"], user ["salary"];

print (get_name());

print_sum (5, 2);

print(get_sum (3, 5));

print(get_sum_positive (4, 5));

print(get_sum_positive (-4, 5));

user_details = {};
user_details["name"] = "Aditya";
user_details["age"] = 34;
user_details["salary"] = 100.84;

print(get_user_data (user_details));

name, age, salary = get_user_data (user_details);
print(name, age, salary);

