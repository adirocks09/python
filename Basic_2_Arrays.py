numbers = [22,44,11,33,19];

print (type(numbers));

size  = len(numbers);

print(numbers, size);

print(numbers[2]);

# print(numbers[10]);

print("\n********************************\n");

for index, value in enumerate (numbers):
  print(index, value);
  print("---------------------");

print("\n********************************\n");

for index, value in enumerate (numbers, start=2):
  print(index, value);
print("---------------------");

print("\n********************************\n");

i = 0;
while i < size:
  if(numbers[i] % 2 == 0) :
    print(f"Even : {numbers[i]}");
  else : 
    print(f"Odd : {numbers[i]}");
  i+=1;

print("\n********************************\n");

even = list(filter(lambda x : x%2==0, numbers));

print(f" Filtered List : {even}");

mapped_data = list(map(lambda x : x*x, numbers));

print(f" Mapped Data List : {mapped_data}");

numbers.sort();

print(numbers);

numbers.append(97);

print(numbers);

numbers.insert(1, 111);

print(numbers);

numbers.remove(22);

print(numbers);