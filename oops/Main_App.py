from Vehicle import Vehicle
from Car import Car
from MiniTruck import MiniTruck
import traceback

print(Vehicle.__doc__) ## Documentation for Vehicle class

lamborgini =  Vehicle("Red_Lambo", "Diesel", 2 )
lamborgini.show_all_instance_properties()
print ("\n.........Properties Added..................\n")
lamborgini.model = "LAMBO777" # adding new property
lamborgini.top_speed = "400 km/hour" # adding new property
lamborgini.show_all_instance_properties()
print ("\n.........Properties Removed..................\n")
del lamborgini.top_speed # deleting property added
lamborgini.show_all_instance_properties()


bolero =  Vehicle("Black_Bolero", "Petrol", 6 )
bolero.registratio_no = 789546 # adding new property

dezire =  Vehicle("White_Dzire", "Electric" )

creta = Car ("Blue_Creta", "Petrol", 5, "Automatic", "Power")
creta.roof_top = True # adding new property
creta.show_all_instance_properties()
creta.show_all_properties()

chota_hathi = MiniTruck ("Yellow_Truck", "Diesel", 2)
chota_hathi.capacity = 122.5 # adding new property

list_of_vehicles = [lamborgini, bolero, dezire, creta, chota_hathi];


try :
  print("\n********************************\n")

  print (lamborgini)
  print (f" seats : {lamborgini.seats} "); # public variables can be directly accessed 
  print (f" color : {lamborgini.get_color()}" ) # private variables can be accessed via getter and setter

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

  print(list_of_vehicles)  # __repr__ is invoked for each object

  print("\n********************************\n")

  for vehicle in enumerate(list_of_vehicles) :
     print(vehicle);  # __repr__ is invoked for each object
  
  print("\n********************************\n")

  for index, vehicle in enumerate(list_of_vehicles) :
     print(vehicle);  # __str__ is invoked for each object

  print("\n********************************\n")

  list_of_vehicles.sort() ## __lt__ is invoked for comparison

  for vehicle in enumerate(list_of_vehicles) :
     print(vehicle);

  #print (1 /0) # throws Exception

  print("\n*************Before Static Data Update*******************\n")

  print (f" Lamborgini : {lamborgini.logger_name}  : {lamborgini.get_wheels()}")
  print (f" Bolero : {bolero.logger_name}  : {bolero.get_wheels()} ")
  print (f" Creta : {creta.logger_name}   : {creta.get_wheels()} ")

  # Static Variable Shared across all objects
  Vehicle.logger_name = "Vehicle_Logger"  # public static variable
  Vehicle.set_wheels(8) # private static variable

  print("\n*************After Static Data Update*******************\n")

  print (f" Lamborgini : {lamborgini.logger_name}  : {lamborgini.get_wheels()}")
  print (f" Bolero : {bolero.logger_name}  : {bolero.get_wheels()} ")
  print (f" Creta : {creta.logger_name}   : {creta.get_wheels()} ")


  print("\n*************Before Instance Data Update*******************\n")

  print (f" Lamborgini : {lamborgini.seats}  : {lamborgini.get_color()}")
  print (f" Bolero : {bolero.seats}  : {bolero.get_color()} ")
  print (f" Creta : {creta.seats}   : {creta.get_color()} ")

  # Static Variable Shared across all objects
  lamborgini.seats = 1  # public instance variable
  lamborgini.set_color("Yellow Lambo") # private instance variable

  print("\n*************After Instance Data Update*******************\n")

  print (f" Lamborgini : {lamborgini.seats}  : {lamborgini.get_color()}")
  print (f" Bolero : {bolero.seats}  : {bolero.get_color()} ")
  print (f" Creta : {creta.seats}   : {creta.get_color()} ")

  print("\n*************Calling Utility Method on the Object *******************\n")

  print (bolero.get_sum(25, 55))


except Exception as e:
    print(f"\n Caught an error! Saving stack trace...\n {e} \n .....................")
    traceback.print_exc()  # similar to e.printStacktrace in Java
    error_stack = traceback.format_exc() # stores error stack trace in string datatype
    print(error_stack)

