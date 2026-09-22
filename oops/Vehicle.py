class Vehicle :

  """
   static variables are written outside constructor function (__init__).
   instance variables are written inside constructor function (__init__).
   private data members are prefixed with double underscore.
   getter and setter methods are required for accessing private data members. 
   "self" is like "this" keyword in java.
   "__str__" method is like "toString()" method in java.
   "__eq__" method is like "equals() method in java"
   "__lt__" method is like "compareTo()" method in java
  
  """

  logger_name = "Vehicle";  # static variable (public)
  __wheels = 4;  # static variable (private)

  def get_wheels() :
    return Vehicle.__wheels;

  def set_wheels(wheels) :
    Vehicle.__wheels = wheels;
  
  def __init__(self, color, engine, seats=4) : # default value assigned to seats as 4 
    self.__color = color  # instance variable (private)
    self.__engine = engine # instance variable (private)
    self.seats = seats # instance variable (public)

  def get_color(self) :
    return self.__color;
  
  def set_color(self, color) :
    self.__color = color;

  def get_engine(self) :
    return self.__engine;

  def set_engine(self, engine) :
    self.__engine = engine;
  
  def __repr__(self) :
    return f" {self.__color}--{self.__engine}--{self.seats}"
  
  def __str__(self) :
    return f" I am a {self.seats} seater,  {self.__color} , {self.__engine} engine vehicle. ";

  def __eq__(self, other) :     
    if(self.__color == other.__color) :
      if(self.__engine == other.__engine) :
        if(self.seats == other.seats) : 
          if (Vehicle.__wheels == other.__wheels) :
            return True;
    else :
       return False;

  def __lt__(self, other):
    return self.seats < other.seats


  
  



