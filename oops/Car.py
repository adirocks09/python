from Vehicle import Vehicle

class Car (Vehicle): 

  __type = "Sedan";

  def __init__(self, color, engine, seats, gearType, steering) :
    super().__init__(color, engine, seats);
    self.__gearType = gearType
    self.__steering = steering
  
  def get_gears(self) : 
    return self.__gearType;

  def set_gears(self, gear) :
    self.__gearType = gear;
  
  def get_steering(self) :
    return self.__steering;

  def set_steering (self, steering) :
    self.__steering = steering;

  def __str__(self) :
    return f" Gears : {self.__gearType},  Steering :  {self.__steering} ";

  def display (self) :
    return super().__str__() + self.__str__();

