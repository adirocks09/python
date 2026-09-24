class Vehicle :

  ## Doc String
  """
     1. Static variables are written outside constructor function (init) and is shared across all objects. 

     2. Instance variables are written inside constructor function (init) and is exclusive for each object,. 

     3. Private data members are prefixed with double underscore.  

     4. Getter and Setter methods are required for accessing private data members.  

     5. "self" is like "this" keyword in java.  

     6. All the instance method and constructor within a class must declare the invoked object as it’s first implicit parameter, conventionally called as “self”, since python always internally injects the invoking object instance as its first parameter during invocation. 

     7. A class method annotated with @classmethod takes the class as its default first implicit parameter, conventionally named “cls” 

     8. If we want to write utility methods and dont want to pass "self" or “cls” as first parameter, then the method must be annotated with @staticmethod  

     9. "str" method is like "toString()" method in java.  

     10. "repr" method is used for representation of object to Developers and also behaves like "toString()" method in java.  

     11. "eq" method is like "equals() method in java". 

     12. "lt" method is like "compareTo()" method in java. 

     13. "show_all_instance_properties" method converts object to dictionary with property_key and property_value. 

     14. "show_all_properties" method converts object to list of property_key. 

  """

  logger_name = "Vehicle"  # static variable (public)
  __wheels = 4  # static variable (private)
  
  def __init__(self, color, engine, seats=4) : # default value assigned to seats as 4 
    self.__color = color  # instance variable (private)
    self.__engine = engine # instance variable (private)
    self.seats = seats # instance variable (public)

  # Class Methods for accessing static variables 
  @classmethod
  def get_wheels(cls) :
    return cls.__wheels
  
  @classmethod
  def set_wheels(cls, wheels) :
    cls.__wheels = wheels  

  # Utility Methods
  @staticmethod  
  def get_sum(a : int, b: int) -> int :
    return a + b  

  # Instance Methods for accessing instance variables 
  def get_color(self) :
    return self.__color
  
  def set_color(self, color) :
    self.__color = color

  def get_engine(self) :
    return self.__engine

  def set_engine(self, engine) :
    self.__engine = engine
  
  # __str__ is for users and focuses on readability,
  # __repr__ is for developers and focuses on providing an unambiguous representation of the object
  # When creating custom classes, the general best practice is to always implement __repr__ first. This ensures you have helpful debug info, and because __str__ falls back to __repr__, you get basic print support automatically.
  # if __str__ is not implemented , print(obj) will invoke __repr__ method

  def __repr__(self) :
    return f" {self.__color}--{self.__engine}--{self.seats}"
  
  def __str__(self) :
    return f" I am a {self.seats} seater,  {self.__color} , {self.__engine} engine vehicle. ";

  def __eq__(self, other) :     
    if(self.__color == other.__color) :
      if(self.__engine == other.__engine) :
        if(self.seats == other.seats) : 
          if (Vehicle.__wheels == other.__wheels) :
            return True
    else :
       return False

  def __lt__(self, other):
    return self.seats < other.seats
  
  def show_all_instance_properties (self) :
   print ("\n***************show_all_instance_properties*******************\n")
   obj_dict = vars(self) # converting object to dictionary
   for key, value in obj_dict.items() :
      print(f"{key} = {value}")


  def show_all_properties (self) :
   print ("\n***************show_all_properties*******************\n")
   obj_dir = dir(self) # converts object to list
   obj_dir.sort()
   for index, value in enumerate(obj_dir) :
      print(f"{index} :: {value}")


  
  



