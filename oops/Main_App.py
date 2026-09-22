from Vehicle import Vehicle
from Car import Car
from MiniTruck import MiniTruck
import traceback


lamborgini =  Vehicle("Red_Lambo", "Diesel", 2 )

bolero =  Vehicle("Black_Bolero", "Petrol", 6 )

dezire =  Vehicle("White_Dzire", "Electric" )

creta = Car ("Blue_Creta", "Petrol", 5, "Automatic", "Power")

chota_hathi = MiniTruck ("Yellow_Truck", "Diesel", 2)

list_of_vehicles = [lamborgini, bolero, dezire, creta, chota_hathi];


try :
  print("\n********************************\n")

  print (lamborgini)
  print (f" seats : {lamborgini.seats} ");
  print (f" color : {lamborgini.get_color()}" )

  print("\n********************************\n")

  print (bolero)

  print("\n********************************\n")

  print (dezire)

  print("\n********************************\n")

  print (creta)
  print (f" seats : {creta.seats} ");
  print (f" color : {creta.get_color()}" )
  print (creta.display())

  print("\n********************************\n")

  print (chota_hathi)

  print("\n********************************\n")

  print(list_of_vehicles)

  print("\n********************************\n")

  for vehicle in enumerate(list_of_vehicles) :
     print(vehicle);
  
  print("\n********************************\n")

  for index, vehicle in enumerate(list_of_vehicles) :
     print(vehicle);

  print("\n********************************\n")

  list_of_vehicles.sort()

  for vehicle in enumerate(list_of_vehicles) :
     print(vehicle);

  # print (1 /0) # throws Exception

except :
    print("Caught an error! Saving stack trace...")
    traceback.print_exc()  # similar to e.printStacktrace in Java
    error_stack = traceback.format_exc() # stores error stack trace in string datatype
    print(error_stack)