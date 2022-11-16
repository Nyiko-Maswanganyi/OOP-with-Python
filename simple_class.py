#create a class called car
class car:
#properties of the class
  def __init__(self, color, model):
    self.color = color
    self.model = model
  
  #this is a class method
  def color_model(self):
   print ("the color of this car is: "+ self.color+" and the name of the model is:"+self.model)

#declare a class object and use it to initialize the variables in the class
p=car("red","Volvo")

p.color_model()
   

 
