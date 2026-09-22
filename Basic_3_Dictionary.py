user_details = {};

user_details["name"] = "Aditya";
user_details["age"] = 34;
user_details["salary"] = 100.84;

print (type(user_details));

print(user_details);

print("\n********************************\n");

for key, value in user_details.items():
  print(f"{key} --> {value}");

print("\n********************************\n");

for key in user_details.keys():
  print(key);

print("\n********************************\n");

for value in user_details.values() :
  print(value);

print("\n********************************\n");

print (user_details["name"]);

print (user_details.get("salary"));

print("\n********************************\n");

user_details.pop("salary");

print(user_details);

print("\n********************************\n");

user_details.clear();

print(user_details);

print("\n********************************\n");




